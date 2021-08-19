FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements/requirements.txt
RUN pip install --no-cache-dir -r /requirements/requirements.txt \
    && rm -rf /requirements

WORKDIR /code
COPY . /code/