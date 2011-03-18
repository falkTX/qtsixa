# You know, there are pre-compile DEBs of this...


all:build

build:
	make -C qtsixa
	make -C utils
	make -C sixad

clean:
	make clean -C qtsixa
	make clean -C utils
	make clean -C sixad

install:
	make install -C qtsixa
	make install -C utils
	make install -C sixad

install-system:
	make install-system -C sixad

uninstall:
	make uninstall -C sixad
	make uninstall -C utils
	make uninstall -C qtsixa

