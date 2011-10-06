/*
 * sixad-bin.cpp
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
#include <iostream>
#include <signal.h>
#include <syslog.h>

int main(int argc, char *argv[])
{
    struct sigaction sa;
    bdaddr_t bdaddr;
    int ctl, csk, isk, debug, legacy, remote;

    if (argc > 3) {
      debug = atoi(argv[1]);
      legacy = atoi(argv[2]);
      remote = atoi(argv[3]);
    } else {
      std::cerr << argv[0] << " requires 'sixad'. Please run sixad instead" << std::endl;
      return 1;
    }

    open_log("sixad-bin");
    syslog(LOG_INFO, "started");
    bacpy(&bdaddr, BDADDR_ANY);

    ctl = socket(AF_BLUETOOTH, SOCK_RAW, BTPROTO_HIDP);
    if (ctl < 0) {
        syslog(LOG_ERR, "Can't open HIDP control socket");
        close(ctl);
        return 1;
    }

    memset(&sa, 0, sizeof(sa));
    sa.sa_flags = SA_NOCLDSTOP;

    sa.sa_handler = sig_term;
    sigaction(SIGTERM, &sa, NULL);
    sigaction(SIGINT, &sa, NULL);

    sa.sa_handler = SIG_IGN;
    sigaction(SIGCHLD, &sa, NULL);
    sigaction(SIGPIPE, &sa, NULL);

    if (remote) {
        // BD Remote only

        syslog(LOG_INFO, "BD Remote mode active, hold Enter+Start on your remote now");

        while (!io_canceled()) {
            do_search(ctl, &bdaddr, debug);
            sleep(2);
        }

    } else {
        // Normal behaviour

        csk = l2cap_listen(&bdaddr, L2CAP_PSM_HIDP_CTRL, L2CAP_LM_MASTER, 10);
        if (csk < 0) {
            syslog(LOG_ERR, "Can't listen on HID control channel");
            close(csk);
            close(ctl);
            return 1;
        }

        isk = l2cap_listen(&bdaddr, L2CAP_PSM_HIDP_INTR, L2CAP_LM_MASTER, 10);
        if (isk < 0) {
            syslog(LOG_ERR, "Can't listen on HID interrupt channel");
            close(isk);
            close(csk);
            close(ctl);
            return 1;
        }

        syslog(LOG_INFO, "sixad started, press the PS button now");

        hid_server(ctl, csk, isk, debug, legacy);

        close(isk);
        close(csk);
    }

    close(ctl);
    syslog(LOG_INFO, "Done");

    return 0;
}
