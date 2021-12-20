#!/bin/bash

set -a
[ -f .env ] && . .env

# Setup rapi_buy .env file
cp .env.example .env


# Build rapi_buy api image
docker build -f Dockerfile  -t rapi_buy/api:latest .
