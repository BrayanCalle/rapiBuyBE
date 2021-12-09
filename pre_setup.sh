#!/bin/bash

set -a
[ -f .env ] && . .env

# Setup b2b .env file
cp .env.example .env


# Build b2b api image
docker build -f ./dockerfiles/Dockerfile --ssh default=$1 -t b2b/api:latest .