# About the project

Rapi Buy

# Docker and Docker Compose installation

Install Docker:

- `https://docs.docker.com/install/`

After install Docker, proceed to install Docker Compose:

- `https://docs.docker.com/compose/install/`

### Project Structure

The following is the suggested structure to successfully build this project:

```
b2b/                           # root project
├── src/                       # django project
├── nginx/                     # nginx conf files
├── Dockerfile                 # django dockerfile
├── docker-compose-dev.yml     # docker compose definition for dev
└── ...
```

## Project Setup

In the following steps we will cover some basic stuff to setup a development environment for rapi buy

### Setup pre-commit hooks

On your current host environment (or global environment) run:

```
$ pip install pre-commit
$ pre-commit install
```

### Building the Project for Development Environment

1. Clone the repository using the follwing command:
```
$ git@github.com:BrayanCalle/rapiBuyBE.git
```
3. Positioned in the root folder execute:
```
$ ./pre_setup.sh
```
4. [DEV-ENV] Run the following commands to allow HTTPS using a self-signed in local env:
```
cd ssl
$ ./self_signed     # Fill with fake data and no passphrase
```
5. Go back to the root folder:
```
$ cd ..
```
6. Run all services with:
```
$ docker-compose -f docker-compose-dev.yml up -d
```
8. API Service should be running on: [https://localhost/api/v1/](https://localhost)
9. Docs Frontend Service (with Hot Reloading) should be running on: [http://localhost:9000](http://localhost:9000)

## Project Basic Commands

### Backend
**Build backend image when new dependencies are being instaled**:

`$ ./build_backend.sh`

**Apply migrations to the DB:**

`$ ./execute manage migrate`

**Create a super-user:**

`$ ./execute manage createsuperuser`

**Collect static files:**

`$ ./execute manage collectstatic`

**Install backend dependencies:**

`$ ./execute install <dependency_name>`
