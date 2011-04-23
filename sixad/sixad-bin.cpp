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

// Globals, needed for search thread
int ctl, debug;
bdaddr_t bdaddr;

void do_search_thread()
{
    while (!io_canceled()) {
        do_search(ctl, &bdaddr, debug);
        usleep(1000);
    }
    pthread_exit((void*)1);
}

int main(int argc, char *argv[])
{
    struct sigaction sa;
    pthread_t search_thread;
    int csk, isk, legacy;

    if (argc > 2) {
      debug = atoi(argv[1]);
      legacy = atoi(argv[2]);
    } else {
      std::cerr << argv[0] << " requires 'sixad'. Please run sixad instead" << std::endl;
      return 1;
    }

    bacpy(&bdaddr, BDADDR_ANY);

    ctl = socket(AF_BLUETOOTH, SOCK_RAW, BTPROTO_HIDP);
    if (ctl < 0) {
        std::cerr << "Can't open HIDP control socket" << std::endl;
        close(ctl);
        return 1;
    }

    csk = l2cap_listen(&bdaddr, L2CAP_PSM_HIDP_CTRL, L2CAP_LM_MASTER, 10);
    if (csk < 0) {
        std::cerr << "Can't listen on HID control channel" << std::endl;
        close(csk);
        close(ctl);
        return 1;
    }

    isk = l2cap_listen(&bdaddr, L2CAP_PSM_HIDP_INTR, L2CAP_LM_MASTER, 10);
    if (isk < 0) {
        std::cerr << "Can't listen on HID interrupt channel" << std::endl;
        close(isk);
        close(csk);
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

    if (pthread_create(&search_thread, NULL, (void *(*)(void *))do_search_thread, NULL)) {
        std::cerr << "error starting search thread" << std::endl;
        return 1;
    }

    std::cout << "sixad started, press the PS button now" << std::endl;

//     while (!io_canceled()) {
        hid_server(ctl, csk, isk, debug, legacy);
//     }

    std::cout << "Closing search thread..." << std::endl;

    sig_term(0);

    if (pthread_cancel(search_thread)) {
        std::cerr << "Error canceling search thread" << std::endl;
    }
    else if (pthread_join(search_thread, NULL)) {
        std::cerr << "Error joining search thread" << std::endl;
    }

    close(isk);
    close(csk);
    close(ctl);

    std::cout << "Done" << std::endl;

    return 0;
}
