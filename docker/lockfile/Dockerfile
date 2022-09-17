FROM ubuntu:20.04

LABEL maintainer="aureliano.buendias@outlook.com"
RUN apt-get update -y && apt-get install -y python3 python3-dev python3-pip curl pipenv

WORKDIR /app

ADD Pipfile.lock Pipfile /app/

ENV PIPENV_VENV_IN_PROJECT=1

RUN pipenv install --system --deploy
COPY src .

CMD ["/usr/bin/python3", "run.py"]
