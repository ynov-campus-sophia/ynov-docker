FROM python:slim-bullseye

LABEL maintainer="aureliano.buendias@outlook.com"

ENV database=crypto-executor
ENV host=localhost
ENV user=executor
ENV password=123456
ENV port=5432

RUN apt-get update -y && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir --upgrade pip
RUN pip install pipenv

WORKDIR /app

ADD Pipfile.lock Pipfile /app/

ENV PIPENV_VENV_IN_PROJECT=1

RUN pipenv install --system --deploy
COPY src .

CMD ["/usr/local/bin/python", "datacollect.py"]
