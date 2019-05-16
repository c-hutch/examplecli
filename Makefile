.PHONY: test, dockerbuild, dockerrun, dockerbash

test:
	python -m pytest -v tests

dockerbuild:
	docker build -t examplecli .

dockerrun:
	docker run -it --rm -e DEBUG=True --name examplecli examplecli

dockerbash:
	docker run -it examplecli /bin/bash

dockerrunargs:
	docker run -it --rm  -e DEBUG=True --name examplecli examplecli