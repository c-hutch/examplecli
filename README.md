# A basic example/template for a containerized Python CLI app

[![CircleCI](https://circleci.com/gh/c-hutch/examplecli/tree/master.svg?style=svg)](https://circleci.com/gh/c-hutch/examplecli/tree/master)
[![codecov](https://codecov.io/gh/c-hutch/examplecli/branch/master/graph/badge.svg)](https://codecov.io/gh/c-hutch/examplecli)


## To make a new app

### Clone the repo with a new name (yourapp) 
```bash
git clone git@github.com:c-hutch/examplecli.git yourapp

cd yourapp
```

### Run these make commands in the newly created project

#### rename changes the names in project files to match the name of your project folder (myapp) 
```bash
make rename
```

#### setup creates a Python virtual environment and installs the requirements-dev.txt file
```bash
make setup
```

#### activate the newly created virtual evnironment
```bash
source venv/bin/activate
```

#### run executes the cli app in the virtual environment
```bash
make run
```

#### dockerbuild builds the app as a Docker container (Docker must be installed https://docs.docker.com/install/)
```bash
make dockerbuild
```

#### dockerrun launches the docker image and executes the cli app
```bash
make dockerrun
```
