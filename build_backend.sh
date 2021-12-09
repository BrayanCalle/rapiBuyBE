#!/bin/bash
set -a
[ -f .env ] && . .env

docker build --no-cache -f dockerfiles/Dockerfile -t rapi_buy/api:latest .
