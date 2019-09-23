APPNAME = $(shell basename $(CURDIR))

.PHONY: test, dockerbuild, dockerrun, dockerbash, setup, rename, run

donothing:
	# TODO: Implement help as make default

#rename:
#	find ./tests -name '*.py' -type f -exec sed -i "s/examplecli/$(APPNAME)/g" {} +
#	find ./examplecli -name '*.py' -type f -exec sed -i "s/examplecli/$(APPNAME)/g" {} +
#	sed -i "s/examplecli/$(APPNAME)/g" Dockerfile
#	sed -i "s/examplecli/$(APPNAME)/g" logconfig.yaml
#	mv examplecli/examplecli.py examplecli/$(APPNAME).py
#	mv examplecli $(APPNAME)

setup:
	# TODO: add markdown to explain git clone with a new name to start a new project
	rm -rf venv
	virtualenv venv
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install -r requirements-dev.txt
	pre-commit install

test:
	tox

run:
	python app/main.py -d

dockerbuild:
	docker build -t $(APPNAME) .

dockerrun:
	docker run -it --rm -e DEBUG=True --name $(APPNAME) $(APPNAME)

dockerbash:
	docker run -it $(APPNAME) /bin/ash

dockerrunargs:
	docker run -it --rm  -e DEBUG=True --name $(APPNAME) $(APPNAME)
