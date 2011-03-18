# You know, there are pre-compile DEBs of this...

CC = gcc
CFLAGS = -O2 -Wall
LDFLAGS += -Wl,-Bsymbolic-functions

WANT_JACK = true

all: tools hcid_bin

tools:
	$(CC) $(CFLAGS) $(LDFLAGS) hidraw-dump.c -o bins/hidraw-dump
	$(CC) $(CFLAGS) $(LDFLAGS) sixpair.c -o bins/sixpair -lusb -I/usr/include/libusb-1.0/
	$(CC) $(CFLAGS) $(LDFLAGS) sixpair_kbd.c -o bins/sixpair-kbd -lusb -I/usr/include/libusb-1.0/
ifeq ($(WANT_JACK),true)
	$(CC) $(CFLAGS) $(LDFLAGS) sixad-jack.c -o bins/sixad-jack -ljack -lm
endif

hcid_bin:
	$(MAKE) -C hcid

clean:
	$(MAKE) clean -C hcid
	rm -f *~ bins/*

install:
	install -d $(DESTDIR)/usr/bin/
	install -d $(DESTDIR)/usr/sbin/
	install -m 755 bins/sixpair $(DESTDIR)/usr/sbin/
	install -m 755 bins/sixpair-kbd $(DESTDIR)/usr/sbin/
	install -m 755 bins/hcid $(DESTDIR)/usr/sbin/
	install -m 755 bins/hidraw-dump $(DESTDIR)/usr/sbin/
ifeq ($(WANT_JACK),true)
	install -m 755 bins/sixad-jack $(DESTDIR)/usr/bin/
endif

uninstall:
	rm -f $(DESTDIR)/usr/bin/sixad-jack
	rm -f $(DESTDIR)/usr/sbin/sixpair
	rm -f $(DESTDIR)/usr/sbin/sixpair-kbd
	rm -f $(DESTDIR)/usr/sbin/hcid
	rm -f $(DESTDIR)/usr/sbin/hidraw-dump
