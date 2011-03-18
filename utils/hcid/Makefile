# Compile hcid binary only

CC = gcc
CFLAGS = -O2 -Wall -fno-strict-aliasing
LDFLAGS += -Wl,-Bsymbolic-functions

PKG_FLAGS = `pkg-config --cflags dbus-1 glib-2.0 bluez`
PKG_LIBS = `pkg-config --libs dbus-1 glib-2.0 bluez`
INCLUDES = -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include

all: common_so sdpd_so dbus_so main_so

common_so:
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/oui.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/dbus.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/textfile.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/logging.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/dbus-helper.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/error.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/sdp-xml.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/sdp-glib.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/hal-dummy.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c common/notify-inotify.c
	rm -f libhelper.a
	ar cru libhelper.a oui.o dbus.o textfile.o logging.o dbus-helper.o error.o sdp-xml.o sdp-glib.o hal-dummy.o notify-inotify.o
	ranlib libhelper.a
	touch common_so

sdpd_so:
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c sdpd/server.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c sdpd/cstate.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c sdpd/request.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c sdpd/service.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c sdpd/servicedb.c
	rm -f libsdpserver.a
	ar cru libsdpserver.a server.o cstate.o request.o service.o servicedb.o
	ranlib libsdpserver.a
	touch sdpd_so

dbus_so:
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c security.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c storage.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c parser.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c lexer.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c kword.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c server.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c manager.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c adapter.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c device.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c dbus-common.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c dbus-error.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c dbus-database.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c dbus-security.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c dbus-service.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c dbus-test.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c dbus-hci.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c dbus-sdp.c
	rm -f libhciserver.a
	ar cru libhciserver.a security.o storage.o parser.o lexer.o kword.o server.o manager.o adapter.o device.o dbus-common.o dbus-error.o dbus-database.o dbus-security.o dbus-service.o dbus-test.o dbus-hci.o dbus-sdp.o
	ranlib libhciserver.a
	touch dbus_so

main_so: common_so sdpd_so dbus_so
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I. -I./common -I./sdpd -I./mod $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) -c main.c
	$(CC) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -o ../bins/hcid main.o libhciserver.a ./libsdpserver.a ./libhelper.a -lbluetooth -ldbus-1 -lglib-2.0 $(INCLUDES) $(CFLAGS) $(PKG_FLAGS) $(LDFLAGS)
	touch main_so

clean:
	rm -rf *.o *.a hcid

