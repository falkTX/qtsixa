# You know, there are pre-compile DEBs of this...

DESTDIR =

all: sixad_bins

sixad_bins:
	g++ -Wall -O2 sixad-bin.cpp bluetooth.cpp shared.cpp textfile.cpp -o bins/sixad-bin -lbluetooth
	g++ -Wall -O2 sixad-sixaxis.cpp sixaxis.cpp shared.cpp uinput.cpp textfile.cpp -o bins/sixad-sixaxis -lpthread
	g++ -Wall -O2 sixad-raw.cpp sixaxis.cpp shared.cpp uinput.cpp textfile.cpp -o bins/sixad-raw

clean:
	rm -f *~ bins/*

install:
	install -d $(DESTDIR)/etc/default/
	install -d $(DESTDIR)/etc/init.d/
	install -d $(DESTDIR)/etc/logrotate.d/
	install -d $(DESTDIR)/usr/bin/
	install -d $(DESTDIR)/usr/sbin/
	install -d $(DESTDIR)/lib/udev/rules.d/
	install -d $(DESTDIR)/var/lib/sixad/
	install -m 644 sixad.default $(DESTDIR)/etc/default/sixad
	install -m 755 sixad.init $(DESTDIR)/etc/init.d/sixad
	install -m 644 sixad.log $(DESTDIR)/etc/logrotate.d/sixad
	install -m 755 sixad $(DESTDIR)/usr/bin/
	install -m 755 bins/sixad-bin $(DESTDIR)/usr/sbin/
	install -m 755 bins/sixad-sixaxis $(DESTDIR)/usr/sbin/
	install -m 755 bins/sixad-raw $(DESTDIR)/usr/sbin/
	install -m 644 98-sixad.rules $(DESTDIR)/lib/udev/rules.d/
	@echo "Please run '[sudo] make install-system' now if you're installing from source"

install-system:
	@addgroup --system sixad || true
	@chown :sixad $(DESTDIR)/var/lib/sixad/
	@chmod 775 -R $(DESTDIR)/var/lib/sixad/
	@echo "Installation is Complete!"
	@echo "You may want to add yourself to the sixad group now:"
	@echo "$ [sudo] adduser YOUR-USER sixad"

uninstall:
	rm -f $(DESTDIR)/etc/default/sixad
	rm -f $(DESTDIR)/etc/init.d/sixad
	rm -f $(DESTDIR)/etc/logrotate.d/sixad
	rm -f $(DESTDIR)/usr/bin/sixad
	rm -f $(DESTDIR)/usr/sbin/sixad-bin
	rm -f $(DESTDIR)/usr/sbin/sixad-sixaxis
	rm -f $(DESTDIR)/usr/sbin/sixad-raw
	rm -f $(DESTDIR)/lib/udev/rules.d/98-sixad.rules
	rm -rf $(DESTDIR)/var/lib/sixad/
