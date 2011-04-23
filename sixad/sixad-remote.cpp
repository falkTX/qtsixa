/*
 * sixad-sixaxis.cpp
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

#include "shared.h"
#include "uinput.h"

#include <cstdlib>
#include <iostream>
#include <poll.h>
#include <signal.h>
#include <string.h>
#include <syslog.h>
#include <time.h>
#include <sys/socket.h>

int fd;
int csk = 0;
int isk = 1;
int debug;
int timeout = 30;

volatile bool active = false;

static int get_time()
{
  timespec tp;
  if (!clock_gettime(CLOCK_MONOTONIC, &tp)) {
    return tp.tv_sec/60;
  } else {
    return -1;
  }
}

static void process_remote(const char *mac)
{
    int br;
    bool msg = true;
    unsigned char buf[64];

    int last_time_action = get_time();

    while (!io_canceled()) {
        br = read(isk, buf, sizeof(buf));
        if (msg) {
            syslog(LOG_INFO, "Connected 'PLAYSTATION(R)3 Remote (%s)'", mac);
            msg = false;
        }

//         if (settings.timeout.enabled) {
          int current_time = get_time();
          if (was_active()) {
            last_time_action = current_time;
            set_active(false);
          } else if (current_time-last_time_action >= 30) {
            syslog(LOG_INFO, "Remote was not in use, and timeout reached, disconneting...");
            sig_term(0);
            break;
          }
//         }

        if (br < 0) {
            break;
        } else {
            // do stuff
        }
    }

    if (debug) syslog(LOG_ERR, "Read loop was broken on the Remote process");
}

int main(int argc, char *argv[])
{
    struct pollfd p[3];
    struct timespec timeout;
    struct sigaction sa;
    sigset_t sigs;
    short events;

    if (argc < 3) {
        std::cout << "Running " << argv[0] << " requires 'sixad'. Please run sixad instead" << std::endl;
        return 1;
    }

    const char *mac = argv[1];
    debug = atoi(argv[2]);

    open_log("sixad-remote");
    
    struct device_settings settings;
    settings.joystick.enabled = true;
    settings.joystick.buttons = true;
    settings.joystick.axis = false;
    settings.joystick.sbuttons = false;
    settings.joystick.accel = false;
    settings.joystick.accon = false;
    settings.joystick.speed = false;
    settings.joystick.pos = false;
    settings.input.enabled = false;
    settings.rumble.enabled = false;

    fd = uinput_open(JS_TYPE_REMOTE, mac, settings);

    if (fd < 0)
        return 1;

    sigfillset(&sigs);
//    sigdelset(&sigs, SIGCHLD);
//    sigdelset(&sigs, SIGPIPE);
//    sigdelset(&sigs, SIGTERM);
//    sigdelset(&sigs, SIGINT);
//    sigdelset(&sigs, SIGHUP);

    memset(&sa, 0, sizeof(sa));
    sa.sa_flags = SA_NOCLDSTOP;

    sa.sa_handler = sig_term;
    sigaction(SIGTERM, &sa, NULL);
    sigaction(SIGINT, &sa, NULL);

    sa.sa_handler = SIG_IGN;
    sigaction(SIGCHLD, &sa, NULL);
    sigaction(SIGPIPE, &sa, NULL);

    p[0].fd = 0;
    p[0].events = POLLIN | POLLERR | POLLHUP;

    p[1].fd = 1;
    p[1].events = POLLIN | POLLERR | POLLHUP;

    p[2].fd = fd;
    p[2].events = POLLIN | POLLERR | POLLHUP;

    while (!io_canceled()) {
        int i, idx = 3;
        for (i = 0; i < idx; i++)
            p[i].revents = 0;

        timeout.tv_sec = 1;
        timeout.tv_nsec = 0;

        if (ppoll(p, idx, &timeout, &sigs) < 1)
            continue;

        if (p[1].revents & POLLIN) {
            process_remote(mac);
        }

        events = p[0].revents | p[1].revents | p[2].revents;

        if (events & (POLLERR | POLLHUP)) {
            break;
        }
    }

    if (debug) syslog(LOG_INFO, "Closing uinput...");
    uinput_close(fd, debug);
    if (debug) syslog(LOG_INFO, "Done");

    return 0;
}
