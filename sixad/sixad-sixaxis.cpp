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
#include "sixaxis.h"
#include "uinput.h"

#include <cstdlib>
#include <iostream>
#include <poll.h>
#include <signal.h>
#include <string.h>
#include <syslog.h>
#include <sys/socket.h>

int fd;
int csk = 0;
int isk = 1;
int debug;

int led_n;
bool old_rumble_mode;

volatile bool active = false;
volatile int weak = 0;
volatile int strong = 0;
volatile int timeout = 0;

static void uinput_listen()
{
        struct input_event event;
        struct uinput_ff_upload upload;
        struct uinput_ff_erase erase;
        struct rumble_effects effects[MAX_RUMBLE_EFFECTS];
        int i;

        //reset effects
        for (i=0; i<MAX_RUMBLE_EFFECTS; i++) {
            effects[i].id = -2;
        }

        while (!io_canceled()) {
                if (read(fd, &event, sizeof event) != sizeof event) {
                        syslog(LOG_INFO, "uinput_listen::Error on uinput read");
                        continue;
                }

                if (debug) syslog(LOG_INFO, "GOT event :: type is %i; code is %i; value is %i\n", event.type, event.code, event.value);

                switch (event.type) {
                case EV_UINPUT:
                        switch (event.code) {
                        case UI_FF_UPLOAD:
                                memset(&upload, 0, sizeof(upload));
                                upload.request_id = event.value;
                                if (ioctl(fd, UI_BEGIN_FF_UPLOAD, &upload) < 0) {
                                        syslog(LOG_ERR, "uinput_listen::Error on ff upload begin");
                                }
                                weak = upload.effect.u.rumble.weak_magnitude/0x101;
                                strong = upload.effect.u.rumble.strong_magnitude/0x101;
                                timeout = upload.effect.replay.length/0x101;
                                if (!old_rumble_mode) {
                                    for (i=0; i<MAX_RUMBLE_EFFECTS; i++) {
                                        if (effects[i].id == -2) {
                                            effects[i].id = upload.effect.id;
                                            effects[i].weak = weak;
                                            effects[i].strong = strong;
                                            effects[i].timeout = timeout;
                                            if (debug) syslog(LOG_INFO, "going for effect #%i", i);
                                            break;
                                        }
                                    }
                                } else {
                                    active = true;
                                }
                                upload.retval = 0;
                                if (ioctl(fd, UI_END_FF_UPLOAD, &upload) < 0) {
                                        syslog(LOG_ERR, "uinput_listen::Error on ff upload end");
                                }
                                break;
                        case UI_FF_ERASE:
                                memset(&erase, 0, sizeof(erase));
                                erase.request_id = event.value;
                                if (ioctl(fd, UI_BEGIN_FF_ERASE, &erase) < 0) {
                                        syslog(LOG_ERR, "uinput_listen::Error on ff erase begin");
                                }
                                if (!old_rumble_mode) {
                                    for (i=0; i<MAX_RUMBLE_EFFECTS; i++) {
                                        if (effects[i].id == event.value) {
                                            effects[i].id = -2;
                                            break;
                                        }
                                    }
                                } else {
                                    weak = 0;
                                    strong = 0;
                                    timeout = 0;
                                    active = true;
                                }
                                erase.retval = 0;
                                if (ioctl(fd, UI_END_FF_ERASE, &erase) < 0) {
                                        syslog(LOG_ERR, "uinput_listen::Error on ff erase end");
                                }
                                break;
                        default:
                                break;
                        }
                        break;
                case EV_FF:
                        if (event.value) {
                            for (i=0; i<MAX_RUMBLE_EFFECTS; i++) {
                                if (effects[i].id == event.code) {
                                    do_rumble(csk, led_n, effects[i].weak, effects[i].strong, effects[i].timeout);
                                    if (debug) syslog(LOG_INFO, "RUMBLE now :: %i|%i|%i", effects[i].weak, effects[i].strong, effects[i].timeout);
                                    break;
                                }
                            }
                        } else {
                           if (!old_rumble_mode) {
                                do_rumble(csk, led_n, 0, 0, 0);
                                if (debug) syslog(LOG_INFO, "RUMBLE clean");
                           }
                        }
                        break;
                default:
                        break;
                }
        }

        pthread_exit((void*)1);
}

static void rumble_listen()
{
    while (!io_canceled()) {
        if (active) {
            do_rumble(csk, led_n, weak, strong, timeout);
            active = false;
        } else
            usleep(500);
    }

    pthread_exit((void*)1);
}

static void process_sixaxis(struct device_settings settings, const char *mac)
{
    int br;
    bool msg = true;
    unsigned char buf[128];
    while (!io_canceled()) {
        br = read(isk, buf, sizeof(buf));
        if (msg) {
            syslog(LOG_INFO, "Connected 'PLAYSTATION(R)3 Controller (%s)' [Battery %02X]", mac, buf[31]);
            msg = false;
        }

        if (br < 0) {
            break;
        } else if (br==50 && buf[0]==0xa1 && buf[1]==0x01 && buf[2]==0x00) { //only continue if we've got a Sixaxis
            if (settings.joystick.enabled) do_joystick(fd, buf, settings.joystick);
            if (settings.input.enabled) do_input(fd, buf, settings.input);
        } else if (br==50 && buf[0]==0xa1 && buf[1]==0x01 && buf[2]==0xff) {
            if (debug) syslog(LOG_ERR, "Got 0xff Sixaxis buffer");
        } else if (buf[0]==0xa1 && buf[1]==0x01 && buf[2]==0x00) {
            syslog(LOG_ALERT, "Sixaxis out of battery!");
            break;
        } else {
            if (debug) syslog(LOG_ERR, "Non-Sixaxis packet received and ignored (0x%02x|0x%02x|0x%02x)", buf[0], buf[1], buf[2]);
        }
    }

    if (debug) syslog(LOG_ERR, "Read loop was broken on the Sixaxis process");
}

int main(int argc, char *argv[])
{
    struct pollfd p[3];
    struct timespec timeout;
    struct device_settings settings;
    struct sigaction sa;
    pthread_t uinput_listen_thread, rumble_listen_thread;
    sigset_t sigs;
    short events;

    if (argc < 3) {
        std::cout << "Running " << argv[0] << " requires 'sixad'. Please run sixad instead" << std::endl;
        return 1;
    }

    const char *mac = argv[1];
    debug = atoi(argv[2]);

    open_log("sixad-sixaxis");
    settings = init_values(mac);

    fd = uinput_open(JS_TYPE_SIXAXIS, mac, settings);

    if (fd < 0)
        return 1;

    enable_sixaxis(csk);
    led_n = set_sixaxis_led(csk, settings.led, settings.rumble.enabled);

    if (settings.rumble.enabled) {
      old_rumble_mode = settings.rumble.old_mode;
      if (pthread_create(&uinput_listen_thread, NULL, (void *(*)(void *))uinput_listen, NULL)) {
              syslog(LOG_ERR, "error starting uinput listen thread");
              return 1;
      }
      if (settings.rumble.old_mode) {
          if (pthread_create(&rumble_listen_thread, NULL, (void *(*)(void *))rumble_listen, NULL)) {
              syslog(LOG_ERR, "error starting rumble listen thread");
              return 1;
          }
      }
    }

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
            process_sixaxis(settings, mac);
        }

        events = p[0].revents | p[1].revents | p[2].revents;

        if (events & (POLLERR | POLLHUP)) {
            break;
        }
    }

    if (settings.rumble.enabled) {
      if (pthread_cancel(uinput_listen_thread)) {
              syslog(LOG_ERR, "Error canceling uinput listen thread");
      }
      else if (pthread_join(uinput_listen_thread, NULL)) {
              syslog(LOG_ERR, "Error joining uinput listen thread");
      }
      if (settings.rumble.old_mode) {
          if (pthread_cancel(rumble_listen_thread)) {
              syslog(LOG_ERR, "Error canceling rumble listen thread");
          }
          else if (pthread_join(rumble_listen_thread, NULL)) {
              syslog(LOG_ERR, "Error joining rumble listen thread");
          }
      }
    }

    if (debug) syslog(LOG_INFO, "Closing uinput...");
    uinput_close(fd, debug);
    if (debug) syslog(LOG_INFO, "Done");

    return 0;
}
