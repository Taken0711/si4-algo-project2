all: build
	echo -e "#!/bin/sh\npython3 algo.py" > algo.ex
	echo -e "#!/bin/sh\npython3 exemple.py" > stat.ex
	chmod +x algo.ex stat.ex

build: analytics.py algo.py exemple.py source/BinList.py source/implem.py
	python3 -m compileall $?

clean:
	rm algo.ex stat.ex
