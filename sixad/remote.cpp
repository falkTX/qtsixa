/*
 * remote.cpp
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

#include "remote.h"
#include "uinput.h"
#include "shared.h"

#include <syslog.h>
#include <sys/socket.h>
#include <unistd.h>

int b1, b2, b3;

void do_joystick(int fd, unsigned char* buf, struct dev_joystick joystick)
{
#if 0
    b1 = buf[3];
    b2 = buf[4];
    b3 = buf[5];

    if (joystick.buttons) {
        //part1
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 0, b1 & 1);
        b1 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 1, b1 & 1);
        b1 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 2, b1 & 1);
        b1 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 3, b1 & 1);
        b1 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 4, b1 & 1);
        b1 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 5, b1 & 1);
        b1 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 6, b1 & 1);
        b1 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 7, b1 & 1);
        //part2
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 8, b2 & 1);
        b2 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 9, b2 & 1);
        b2 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 10, b2 & 1);
        b2 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 11, b2 & 1);
        b2 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 12, b2 & 1);
        b2 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 13, b2 & 1);
        b2 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 14, b2 & 1);
        b2 >>= 1;
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 15, b2 & 1);
        //part3
        uinput_send(fd, EV_KEY, BTN_JOYSTICK + 16, b3 & 1);

        if (b1 > 0 || b2 > 0 || b3 > 0) {
          set_active(true);
        }
    }

    uinput_send(fd, EV_SYN, SYN_REPORT, 0);
#endif
}

void do_remote(int fd, unsigned char* buf, struct dev_remote remote)
{
#if 0
    //TODO
#endif
}

void do_input(int fd, unsigned char* buf, struct dev_input input)
{
#if 0
    b1 = buf[3];
    b2 = buf[4];
    b3 = buf[5];

    //part1
    if (input.key_select) uinput_send(fd, EV_KEY, input.key_select, b1 & 1);
    b1 >>= 1;
    if (input.key_l3) uinput_send(fd, EV_KEY, input.key_l3, b1 & 1);
    b1 >>= 1;
    if (input.key_r3) uinput_send(fd, EV_KEY, input.key_r3, b1 & 1);
    b1 >>= 1;
    if (input.key_start) uinput_send(fd, EV_KEY, input.key_start, b1 & 1);
    b1 >>= 1;
    if (input.key_up) uinput_send(fd, EV_KEY, input.key_up, b1 & 1);
    b1 >>= 1;
    if (input.key_right) uinput_send(fd, EV_KEY, input.key_right, b1 & 1);
    b1 >>= 1;
    if (input.key_down) uinput_send(fd, EV_KEY, input.key_down, b1 & 1);
    b1 >>= 1;
    if (input.key_left) uinput_send(fd, EV_KEY, input.key_left, b1 & 1);
    //part2
    if (input.key_l2) uinput_send(fd, EV_KEY, input.key_l2, b2 & 1);
    b2 >>= 1;
    if (input.key_r2) uinput_send(fd, EV_KEY, input.key_r2, b2 & 1);
    b2 >>= 1;
    if (input.key_l1) uinput_send(fd, EV_KEY, input.key_l1, b2 & 1);
    b2 >>= 1;
    if (input.key_r1) uinput_send(fd, EV_KEY, input.key_r1, b2 & 1);
    b2 >>= 1;
    if (input.key_tri) uinput_send(fd, EV_KEY, input.key_tri, b2 & 1);
    b2 >>= 1;
    if (input.key_cir) uinput_send(fd, EV_KEY, input.key_cir, b2 & 1);
    b2 >>= 1;
    if (input.key_cro) uinput_send(fd, EV_KEY, input.key_cro, b2 & 1);
    b2 >>= 1;
    if (input.key_squ) uinput_send(fd, EV_KEY, input.key_squ, b2 & 1);
    //part3
    if (input.key_ps) uinput_send(fd, EV_KEY, input.key_ps, b3 & 1);

    if (b1 > 0 || b2 > 0 || b3 > 0) {
      set_active(true);
    }

    uinput_send(fd, EV_SYN, SYN_REPORT, 0);
#endif
}
