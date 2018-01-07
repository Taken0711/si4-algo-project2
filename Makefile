all: build
	echo "#!/bin/sh" > algo.ex
	echo "python3 source/algo.py $@" >> algo.ex
	echo "#!/bin/sh" > stat.ex
	echo "python3 source/exemple.py $@" >> stat.ex
	echo "#!/bin/sh" > analytics.ex
	echo "python3 source/analytics.py $@" >> analytics.ex
	chmod +x *.ex


build: source/analytics.py source/algo.py source/exemple.py source/BinList.py source/implem.py
	python3 -m compileall $?

clean:
	rm *.ex
