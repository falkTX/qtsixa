/*
 * sixaxis.h
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

#ifndef SIXAXIS_H
#define SIXAXIS_H

struct rumble_effects {
    int id;
    int weak;
    int strong;
    int timeout;
};

void do_joystick(int fd, unsigned char* buf, struct dev_joystick joystick);
void do_input(int fd, unsigned char* buf, struct dev_input input);
void do_rumble(int csk, int led_n, int weak, int strong, int timeout);

int set_sixaxis_led(int csk, struct dev_led led, int rumble);

#endif // SIXAXIS_H
