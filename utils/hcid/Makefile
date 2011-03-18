#Compile hcid binary only

all: common_so sdpd_so dbus_so main_so

common_so:
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/oui.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/dbus.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/textfile.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/logging.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/dbus-helper.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/error.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/sdp-xml.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/sdp-glib.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/hal-dummy.c
	cc -DHAVE_CONFIG_H -I. -I./mod   -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c common/notify-inotify.c
	rm -f libhelper.a
	ar cru libhelper.a oui.o dbus.o textfile.o logging.o dbus-helper.o error.o sdp-xml.o sdp-glib.o hal-dummy.o notify-inotify.o 
	ranlib libhelper.a


sdpd_so:
	cc -DHAVE_CONFIG_H -I. -I./common -I./mod  -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c sdpd/server.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./mod  -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c sdpd/cstate.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./mod  -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c sdpd/request.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./mod  -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c sdpd/service.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./mod  -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c sdpd/servicedb.c
	rm -f libsdpserver.a
	ar cru libsdpserver.a server.o cstate.o request.o service.o servicedb.o 
	ranlib libsdpserver.a

dbus_so:
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c security.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c storage.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c parser.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c lexer.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c kword.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c server.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c manager.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c adapter.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c device.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c dbus-common.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c dbus-error.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c dbus-database.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c dbus-security.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c dbus-service.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c dbus-test.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c dbus-hci.c
	cc -DHAVE_CONFIG_H -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c dbus-sdp.c
	rm -f libhciserver.a
	ar cru libhciserver.a security.o storage.o parser.o lexer.o kword.o server.o manager.o adapter.o device.o dbus-common.o dbus-error.o dbus-database.o dbus-security.o dbus-service.o dbus-test.o dbus-hci.o dbus-sdp.o
	ranlib libhciserver.a

main_so:
	cc -DHAVE_CONFIG_H -I. -I. -I./common -I./sdpd -I./mod  -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include   -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include   -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -c main.c
	cc -I/usr/include/dbus-1.0 -I/usr/lib/dbus-1.0/include -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include -g -O2 -g -Wall -O2 -D_FORTIFY_SOURCE=2 -Wl,-Bsymbolic-functions -o ../bins/hcid main.o  libhciserver.a ./libsdpserver.a ./libhelper.a /usr/lib/libglib-2.0.so -ldbus-1 /usr/lib/libbluetooth.so

clean:
	rm -rf *.o *.a hcid

