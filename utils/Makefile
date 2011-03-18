# You know, there are pre-compile DEBs of this...

DESTDIR =

all: tools hcid_bin

tools:
	gcc -Wall -O2 hidraw-dump.c -o bins/hidraw-dump
	gcc -Wall -O2 sixad-jack.c -o bins/sixad-jack -ljack -lm
	gcc -Wall -O2 sixpair.c -o bins/sixpair -lusb -I/usr/include/libusb-1.0/
	gcc -Wall -O2 sixpair_kbd.c -o bins/sixpair-kbd -lusb

hcid_bin:
	make -C hcid

clean:
	make clean -C hcid
	rm -f *~ bins/*

install:
	install -d $(DESTDIR)/usr/bin/
	install -d $(DESTDIR)/usr/sbin/
	install -m 655 bins/sixad-jack $(DESTDIR)/usr/bin/
	install -m 655 bins/sixpair $(DESTDIR)/usr/sbin/
	install -m 655 bins/sixpair-kbd $(DESTDIR)/usr/sbin/
	install -m 655 bins/hcid $(DESTDIR)/usr/sbin/
	install -m 655 bins/hidraw-dump $(DESTDIR)/usr/sbin/

uninstall:
	rm -f $(DESTDIR)/usr/bin/sixad-jack
	rm -f $(DESTDIR)/usr/bin/sixpair
	rm -f $(DESTDIR)/usr/bin/sixpair-kbd
	rm -f $(DESTDIR)/usr/sbin/hcid
	rm -f $(DESTDIR)/usr/sbin/hidraw-dump
