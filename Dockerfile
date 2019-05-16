FROM python:3.7.3-alpine3.9

WORKDIR /usr/src/app


ENV PATH "${PATH}:/usr/src/app"
ENV PYTHONPATH /usr/src/app

COPY requirements.txt logconfig.yaml ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache bash

COPY ./examplecli ./examplecli

CMD [ "python", "-m", "examplecli.cli"]
