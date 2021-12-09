FROM python:3.9-slim-buster
MAINTAINER "Bryan Calle"

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    && apt-get install -y --no-install-recommends git openssh-client \
    && apt-get install gcc -y

ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/backend
WORKDIR /opt/backend
RUN useradd -m container_user
RUN mkdir /opt/logs
COPY ./src .
RUN chown -R container_user:container_user /opt/backend
RUN chown -R container_user:container_user /opt/logs


RUN pip3 install pipenv
# Run pipenv install with ssh forwarded from host
RUN --mount=type=ssh,id=default pipenv install --system

EXPOSE 8000

ENTRYPOINT ["/opt/backend/entrypoint.sh"]
