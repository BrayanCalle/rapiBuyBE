#!/bin/bash
set -a
[ -f .env ] && . .env

docker build --no-cache -f Dockerfile -t rapi_buy/api:latest .
