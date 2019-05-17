APPNAME = $(shell basename $(CURDIR))

.PHONY: test, dockerbuild, dockerrun, dockerbash, setup, rename, run

donothing:
	# TODO: Implement help as make default

setup:
	rm -rf venv
	virtualenv venv
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install -r requirements-dev.txt

test:
	python -m pytest -v tests

run:
	python -m $(APPNAME).cli -d

dockerbuild:
	docker build -t $(APPNAME) .

dockerrun:
	docker run -it --rm -e DEBUG=True --name $(APPNAME) $(APPNAME)

dockerbash:
	docker run -it $(APPNAME) /bin/bash

dockerrunargs:
	docker run -it --rm  -e DEBUG=True --name $(APPNAME) $(APPNAME)