# Compile hcid binary only

CC ?= gcc
CFLAGS ?= -O2 -Wall
LDFLAGS += -Wl,-Bsymbolic-functions

PKG_FLAGS:=$(shell pkg-config --cflags dbus-1 glib-2.0 bluez)
PKG_LIBS:=$(shell pkg-config --libs dbus-1 glib-2.0 bluez)

all: common_so sdpd_so dbus_so main_so

common_so:
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/oui.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/dbus.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/textfile.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/logging.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/dbus-helper.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/error.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/sdp-xml.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/sdp-glib.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/hal-dummy.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./mod -c common/notify-inotify.c
	rm -f libhelper.a
	ar cru libhelper.a oui.o dbus.o textfile.o logging.o dbus-helper.o error.o sdp-xml.o sdp-glib.o hal-dummy.o notify-inotify.o
	ranlib libhelper.a
	touch common_so

sdpd_so:
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod -c sdpd/server.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod -c sdpd/cstate.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod -c sdpd/request.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod -c sdpd/service.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./mod -c sdpd/servicedb.c
	rm -f libsdpserver.a
	ar cru libsdpserver.a server.o cstate.o request.o service.o servicedb.o
	ranlib libsdpserver.a
	touch sdpd_so

dbus_so:
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c security.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c storage.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c parser.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c lexer.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c kword.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c server.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c manager.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c adapter.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c device.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c dbus-common.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c dbus-error.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c dbus-database.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c dbus-security.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c dbus-service.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -fno-strict-aliasing -c dbus-test.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c dbus-hci.c
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I./common -I./sdpd -I./mod -c dbus-sdp.c
	rm -f libhciserver.a
	ar cru libhciserver.a security.o storage.o parser.o lexer.o kword.o server.o manager.o adapter.o device.o dbus-common.o dbus-error.o dbus-database.o dbus-security.o dbus-service.o dbus-test.o dbus-hci.o dbus-sdp.o
	ranlib libhciserver.a
	touch dbus_so

main_so: common_so sdpd_so dbus_so
	$(CC) $(CFLAGS) $(PKG_FLAGS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -I. -I. -I./common -I./sdpd -I./mod -c main.c
	$(CC) $(CFLAGS) $(LDFLAGS) $(PKG_FLAGS) $(PKG_LIBS) -DHAVE_CONFIG_H -D_FORTIFY_SOURCE=2 -o ../bins/hcid main.o libhciserver.a ./libsdpserver.a ./libhelper.a
	touch main_so

clean:
	rm -rf *.o *.a hcid main_so common_so sdpd_so dbus_so

