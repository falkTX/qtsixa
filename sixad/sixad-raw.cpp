/*
 * sixad-raw.cpp
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

#include <iostream>
#include <fcntl.h>
#include <syslog.h>

int main(int argc, char **argv)
{
    int i, fd, ufd, nr;
    unsigned char buf[128];
    struct device_settings settings;

    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " /dev/hidrawX" << std::endl;
        return 1;
    }

    if ((fd = open(argv[1], O_RDONLY)) < 0) {
        std::cerr << "sixad-raw::open(hidrawX) - failed to open hidraw device" << std::endl;
        return 1;
    }

    if ((nr=read(fd, buf, sizeof(buf))) < 0) {
        std::cerr << "sixad-raw::read(fd) - failed to read from device" << std::endl;
        return 1;
    }

    if (nr < 49 || nr > 50) {
        std::cerr <<  "sixad-raw::read(fd) - not a sixaxis (nr = " << nr << ")" << std::endl;
        return 1;
    }

    open_log("sixad-raw");
    settings = init_values("hidraw");

    // hidraw has no rumble/led support
    settings.led.enabled = false;
    settings.rumble.enabled = false;

    if (!settings.joystick.enabled && !settings.input.enabled) {
        std::cerr <<  "sixad-raw::init_values() - Both joystick and input modes are disabled. Please enable at least one!" << std::endl;
        return 1;
    }
    if ((ufd = uinput_open(JS_TYPE_SIXAXIS, "hidraw", settings)) < 0) {
        return 1;
    }

    bool msg = true;
    while ( true ) {

        nr=read(fd, buf, sizeof(buf));

        if (nr < 49 || nr > 50) {
          std::cerr <<  "sixad-raw::read(fd, buf) - failed to read from device" << std::endl;
          break;
        } else if (nr == 49) {
          for (i=50; i>0; i--) {
            buf[i] = buf[i-1];
          }
        }

        if (msg) {
            syslog(LOG_INFO, "Connected 'PLAYSTATION(R)3 Controller (hidraw)' [Battery %02X]", buf[31]);
            if (nr == 49) syslog(LOG_INFO, "Notice: non-standard Sixaxis buffer size (49)");
            msg = false;
        }

        if (settings.joystick.enabled) do_joystick(ufd, buf, settings.joystick);
        if (settings.input.enabled) do_input(ufd, buf, settings.input);

    }

    uinput_close(ufd);
    std::cerr <<  "sixad-raw::read(buf) - connection has been broken" << std::endl;

    return 0;
}
