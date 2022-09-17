FROM python:slim-bullseye

LABEL maintainer="aureliano.buendias@outlook.com"
RUN pip install --no-cache-dir --upgrade pip
RUN pip install pipenv

WORKDIR /app

ADD Pipfile.lock Pipfile /app/

ENV PIPENV_VENV_IN_PROJECT=1

RUN pipenv install --system --deploy
COPY src .

CMD ["/usr/local/bin/python", "run.py"]
