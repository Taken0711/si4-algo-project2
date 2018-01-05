all: build
	echo -e "#!/bin/sh\npython3 source/algo.py" > algo.ex
	echo -e "#!/bin/sh\npython3 source/exemple.py" > stat.ex
	chmod +x algo.ex stat.ex

build: source/analytics.py source/algo.py source/exemple.py source/BinList.py source/implem.py
	python3 -m compileall $?

clean:
	rm algo.ex stat.ex
