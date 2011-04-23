/*
 * remote.h
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

#ifndef REMOTE_H
#define REMOTE_H

void do_joystick(int fd, unsigned char* buf, struct dev_joystick joystick);
void do_remote(int fd, unsigned char* buf, struct dev_remote remote);
void do_input(int fd, unsigned char* buf, struct dev_input input);

#endif // REMOTE_H
