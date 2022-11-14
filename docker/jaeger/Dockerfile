FROM python:3.8-alpine as builder

LABEL maintainer="aureliano.buendias@outlook.com"

# Install build dependancies
RUN apk update && apk add --upgrade --no-cache g++ make

RUN pip install --no-cache-dir --upgrade pip
RUN pip install pipenv

WORKDIR /usr/local/src

ADD Pipfile.lock Pipfile /usr/local/src/

RUN PIPENV_VENV_IN_PROJECT=1 pipenv sync

FROM python:3.8-alpine as runtime

# Create the user ynov
RUN addgroup --gid 1000 ynov
RUN adduser --disabled-password --home /home/ynov --ingroup ynov \
            --uid 1000 ynov

USER ynov
WORKDIR /home/ynov
COPY src .
COPY --from=builder /usr/local/src/.venv /home/ynov/.venv

ENTRYPOINT ["./.venv/bin/python", "run.py"]