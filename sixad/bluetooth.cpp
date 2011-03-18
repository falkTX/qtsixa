/*
 * bluetooth.cpp
 *
 * This file is part of the QtSixA, the Sixaxis Joystick Manager
 * Copyright 2008-10 Filipe Coelho <falktx@gmail.com>
 *
 * QtSixA can be redistributed and/or modified under the terms of the GNU General
 * Public License (Version 2), as published by the Free Software Foundation.
 * A copy of the license is included in the QtSixA source code, or can be found
 * online at www.gnu.org/licenses.
 *
 * QtSixA is distributed in the hope that it will be useful, but WITHOUT ANY
 * WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 * A PARTICULAR PURPOSE. See the GNU General Public License for more details.
 *
 */

#include "bluetooth.h"
#include "shared.h"

#include <cstdlib>
#include <cerrno>
#include <iostream>
#include <poll.h>
#include <signal.h>
#include <sys/ioctl.h>

#include <bluetooth/hidp.h>
#include <bluetooth/sdp.h>
#include <bluetooth/sdp_lib.h>

int l2cap_listen(const bdaddr_t *bdaddr, unsigned short psm, int lm, int backlog)
{
    struct sockaddr_l2 addr;
    struct l2cap_options opts;
    int sk;

    if ((sk = socket(PF_BLUETOOTH, SOCK_SEQPACKET, BTPROTO_L2CAP)) < 0)
        return -1;

    memset(&addr, 0, sizeof(addr));
    addr.l2_family = AF_BLUETOOTH;
    bacpy(&addr.l2_bdaddr, bdaddr);
    addr.l2_psm = htobs(psm);

    if (bind(sk, (struct sockaddr *) &addr, sizeof(addr)) < 0) {
        close(sk);
        return -1;
    }

    setsockopt(sk, SOL_L2CAP, L2CAP_LM, &lm, sizeof(lm));

    memset(&opts, 0, sizeof(opts));
    opts.imtu = 64;
    opts.omtu = HIDP_DEFAULT_MTU;
    opts.flush_to = 0xffff;

    setsockopt(sk, SOL_L2CAP, L2CAP_OPTIONS, &opts, sizeof(opts));

    if (listen(sk, backlog) < 0) {
        close(sk);
        return -1;
    }

    return sk;
}

void l2cap_accept(int ctl, int csk, int isk, int debug, int legacy)
{
    struct sockaddr_l2 addr;
    struct hidp_connadd_req req;
    socklen_t addrlen;
    bdaddr_t addr_src, addr_dst;
    int ctrl_socket, intr_socket, err;

    memset(&addr, 0, sizeof(addr));
    addrlen = sizeof(addr);

    if ((ctrl_socket = accept(csk, (struct sockaddr *)&addr, &addrlen)) < 0) {
        std::cerr << "unable to accept control stream" << std::endl;
        return;
    }
    bacpy(&addr_dst, &addr.l2_bdaddr);

    if (getsockname(ctrl_socket, (struct sockaddr *)&addr, &addrlen) < 0) {
        std::cerr << "unable to get socket name from control stream" << std::endl;
        return;
    }
    bacpy(&addr_src, &addr.l2_bdaddr);

    if ((intr_socket = accept(isk, (struct sockaddr *)&addr, &addrlen)) < 0) {
        std::cerr << "unable to accept info stream" << std::endl;
        close(ctrl_socket);
        return;
    }

    if (bacmp(&addr_dst, &addr.l2_bdaddr)) {
        std::cerr << "intr and ctrl streams from different hosts - rejecting both" << std::endl;
        close(ctrl_socket);
        close(intr_socket);
        return;
    }

    get_sdp_device_info(&addr_src, &addr_dst, &req);

    if (!legacy && req.vendor == 0x054c && req.product == 0x0268) {
        if (debug) std::cout << "Will initiate Sixaxis now" << std::endl;

        char bda[18];
        ba2str(&addr_dst, bda);

        const char *uinput_sixaxis_cmd = "/usr/sbin/sixad-sixaxis";
        const char *debug_mode = debug ? "1" : "0";

        dup2(intr_socket, 1);
        close(intr_socket);
        dup2(ctrl_socket, 0);
        close(ctrl_socket);

        close(isk);
        close(csk);
        close(ctl);

        const char *argv[] = { uinput_sixaxis_cmd, bda, debug_mode, NULL };

        std::cout << "Connected PLAYSTATION(R)3 Controller (" << bda << ")" << std::endl;

        if (execve(argv[0], (char* const*)argv, NULL) < 0) {
            std::cerr << "cannot exec " << uinput_sixaxis_cmd << std::endl;
            close(1);
            close(0);
        }
    } else {
        if (debug) std::cout << "Creating new device using the default driver..." << std::endl;
        err = create_device(ctl, ctrl_socket, intr_socket);
        if (err < 0)
            std::cerr << "HID create error " << errno << "(" << strerror(errno) << ")" << std::endl;
        close(intr_socket);
        close(ctrl_socket);
    }
    return;
}

void hid_server(int ctl, int csk, int isk, int debug, int legacy)
{
    struct pollfd p[2];
    struct timespec timeout;
    short events;
    sigset_t sigs;

    sigfillset(&sigs);
    sigdelset(&sigs, SIGCHLD);
    sigdelset(&sigs, SIGPIPE);
    sigdelset(&sigs, SIGTERM);
    sigdelset(&sigs, SIGINT);
    sigdelset(&sigs, SIGHUP);

    if (debug) std::cout << "Server mode active, will start search now" << std::endl;

    p[0].fd = csk;
    p[0].events = POLLIN | POLLERR | POLLHUP;

    p[1].fd = isk;
    p[1].events = POLLIN | POLLERR | POLLHUP;

    while (!io_canceled()) {
        int i, idx = 2;

        for (i=0; i<idx; i++)
            p[i].revents = 0;

        timeout.tv_sec = 1;
        timeout.tv_nsec = 0;

        if (ppoll(p, idx, &timeout, &sigs) < 1)
            continue;

        events = p[0].revents | p[1].revents;

        if (events & POLLIN) {
            if (debug) std::cout << "One event received" << std::endl;
            l2cap_accept(ctl, csk, isk, debug, legacy);
            if (debug) std::cout << "One event proccessed" << std::endl;
        }

        if (events & (POLLERR | POLLHUP)) {
            if (debug) std::cerr << "Server mode loop was broken" << std::endl;
            break;
        }

    }
}

int create_device(int ctl, int csk, int isk)
{
     struct hidp_connadd_req req;
     struct sockaddr_l2 addr;
     socklen_t addrlen;
     bdaddr_t src, dst;
     char bda[18];
     int err;

     memset(&addr, 0, sizeof(addr));
     addrlen = sizeof(addr);

     if (getsockname(csk, (struct sockaddr *) &addr, &addrlen) < 0)
         return -1;

     bacpy(&src, &addr.l2_bdaddr);

     memset(&addr, 0, sizeof(addr));
     addrlen = sizeof(addr);

     if (getpeername(csk, (struct sockaddr *) &addr, &addrlen) < 0)
         return -1;

     bacpy(&dst, &addr.l2_bdaddr);

     memset(&req, 0, sizeof(req));
     req.ctrl_sock = csk;
     req.intr_sock = isk;
     req.flags     = 0;
     req.idle_to   = 1800;

     err = get_sdp_device_info(&src, &dst, &req);
     if (err < 0)
         return err;
     else {
         ba2str(&dst, bda);
         std::cout << "Connected " << req.name << " (" << bda << ")" << std::endl;
         if (req.vendor == 0x054c && req.product == 0x0268)
             enable_sixaxis(csk);
         err = ioctl(ctl, HIDPCONNADD, &req);
     }

  return 0;
}

int get_sdp_device_info(const bdaddr_t *src, const bdaddr_t *dst, struct hidp_connadd_req *req)
{
    struct sockaddr_l2 addr;
    socklen_t addrlen;
    bdaddr_t bdaddr;
    sdp_data_t *pdlist, *pdlist2;
    sdp_list_t *search, *attrid, *pnp_rsp, *hid_rsp;
    sdp_record_t *rec;
    sdp_session_t *sdp_session;
    uuid_t svclass;
    uint32_t range = 0x0000ffff;
    int err;

    sdp_session = sdp_connect(src, dst, SDP_RETRY_IF_BUSY | SDP_WAIT_ON_CLOSE);
    if (!sdp_session) {
        std::cerr << "unable to connect to sdp session" << std::endl;
        return -1;
    }

    sdp_uuid16_create(&svclass, PNP_INFO_SVCLASS_ID);
    search = sdp_list_append(NULL, &svclass);
    attrid = sdp_list_append(NULL, &range);

    err = sdp_service_search_attr_req(sdp_session, search, SDP_ATTR_REQ_RANGE, attrid, &pnp_rsp);

    sdp_list_free(search, NULL);
    sdp_list_free(attrid, NULL);

    sdp_uuid16_create(&svclass, HID_SVCLASS_ID);
    search = sdp_list_append(NULL, &svclass);
    attrid = sdp_list_append(NULL, &range);

    err = sdp_service_search_attr_req(sdp_session, search, SDP_ATTR_REQ_RANGE, attrid, &hid_rsp);

    sdp_list_free(search, NULL);
    sdp_list_free(attrid, NULL);

    memset(&addr, 0, sizeof(addr));
    addrlen = sizeof(addr);

    if (getsockname(sdp_session->sock, (struct sockaddr *) &addr, &addrlen) < 0)
            bacpy(&bdaddr, src);
    else
            bacpy(&bdaddr, &addr.l2_bdaddr);

    sdp_close(sdp_session);

    if (err || !hid_rsp) {
        std::cerr << "unable to get device information" << std::endl;
        return -1;
    }

    if (pnp_rsp) {
        rec = (sdp_record_t *) pnp_rsp->data;

        pdlist = sdp_data_get(rec, 0x0201);
        req->vendor = pdlist ? pdlist->val.uint16 : 0x0000;

        pdlist = sdp_data_get(rec, 0x0202);
        req->product = pdlist ? pdlist->val.uint16 : 0x0000;

        pdlist = sdp_data_get(rec, 0x0203);
        req->version = pdlist ? pdlist->val.uint16 : 0x0000;

        sdp_record_free(rec);
    }

    rec = (sdp_record_t *) hid_rsp->data;

    pdlist = sdp_data_get(rec, 0x0101);
    pdlist2 = sdp_data_get(rec, 0x0102);
    if (pdlist) {
            if (pdlist2) {
                    if (strncmp(pdlist->val.str, pdlist2->val.str, 5)) {
                            strncpy(req->name, pdlist2->val.str, sizeof(req->name) - 1);
                            strcat(req->name, " ");
                    }
                    strncat(req->name, pdlist->val.str,
                                    sizeof(req->name) - strlen(req->name));
            } else
                    strncpy(req->name, pdlist->val.str, sizeof(req->name) - 1);
    } else {
            pdlist2 = sdp_data_get(rec, 0x0100);
            if (pdlist2)
                    strncpy(req->name, pdlist2->val.str, sizeof(req->name) - 1);
    }

    pdlist = sdp_data_get(rec, 0x0201);
    req->parser = pdlist ? pdlist->val.uint16 : 0x0100;

    pdlist = sdp_data_get(rec, 0x0202);
    req->subclass = pdlist ? pdlist->val.uint8 : 0;

    pdlist = sdp_data_get(rec, 0x0203);
    req->country = pdlist ? pdlist->val.uint8 : 0;

    pdlist = sdp_data_get(rec, 0x0206);
    if (pdlist) {
            pdlist = pdlist->val.dataseq;
            pdlist = pdlist->val.dataseq;
            pdlist = pdlist->next;

            req->rd_data = (uint8_t*)malloc(pdlist->unitSize);
            if (req->rd_data) {
                    memcpy(req->rd_data, (unsigned char *) pdlist->val.str, pdlist->unitSize);
                    req->rd_size = pdlist->unitSize;
                    epox_endian_quirk(req->rd_data, req->rd_size);
            }
    }

    sdp_record_free(rec);

    return 0;
}

void epox_endian_quirk(unsigned char *data, int size)
{
        /* USAGE_PAGE (Keyboard)	05 07
         * USAGE_MINIMUM (0)		19 00
         * USAGE_MAXIMUM (65280)	2A 00 FF   <= must be FF 00
         * LOGICAL_MINIMUM (0)		15 00
         * LOGICAL_MAXIMUM (65280)	26 00 FF   <= must be FF 00
         */
        unsigned char pattern[] = { 0x05, 0x07, 0x19, 0x00, 0x2a, 0x00, 0xff,
                                                0x15, 0x00, 0x26, 0x00, 0xff };
        unsigned int i;

        if (!data)
                return;

        for (i = 0; i < size - sizeof(pattern); i++) {
                if (!memcmp(data + i, pattern, sizeof(pattern))) {
                        data[i + 5] = 0xff;
                        data[i + 6] = 0x00;
                        data[i + 10] = 0xff;
                        data[i + 11] = 0x00;
                }
        }
}
