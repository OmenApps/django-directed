# Contributing to django-directed

We welcome contributions that meet the goals and standards of this project. Contributions may include bug fixes, feature development, corrections or additional context for the documentation, submission of Issues on GitHub, etc.

For development and testing, you can run your own instance of Postgres (either locally or using a DBaaS), or you can use the provided Docker Compose yaml file to provision a containerized instance and data volume locally.


## Using Your Own postgres Instance

To develop using your own Postgres instance, you may set the following environmental variables on your machine:

- DB_NAME (defaults to "postgres")
- DB_NAME_WITH_EXTENSIONS (defaults to "postgres_with_extensions")
- DB_USER (defaults to "docker")
- DB_PASSWORD (defaults to "docker")
- DB_HOST (defaults to "localhost")
- DB_PORT (defaults to "9932")

The process of setting environmental variables varies between different operating systems. Generally, on macOS and Linux, you can use the following convention in the console:

```bash
export KEY=value
```

## Using the Provided Docker Compose Postgres Instance

This guide assumes you already have [Docker and Docker Compose installed](https://docs.docker.com/compose/install/).

### Build & Bring up the Docker Compose container for Postgres services:

Run the following command to build and bring up the postgres service.

```bash
docker-compose -f dev.yml up -d --no-deps --force-recreate --build postgres
```

These are the database connection details:

    DB = postgres *and* postgres_with_extensions
    USER = docker
    PASSWORD = docker
    HOST = postgres
    PORT = 9932

Note that the docker-compose postgres service creates two databases:

- The default `postgres` database with default functionality. In Django tests, this is the `default` database.
- A database named `postgres_with_extensions`, which has the plpython3u extension installed. In Django tests, this is the `with_extensions` database.

*(The PL/Python procedural language is used in tests of advanced backend functionality which can make use of python-based graph libraries)*

### To check the status of the database container:

```bash
docker ps
```

Once running, you should be able to connect using the test app, psql, or other Postgres management tools if desired.

### To completely remove the container and associated data:

```bash
docker-compose -f dev.yml down --rmi all --remove-orphans -v
```

## Once you have a Running Postgres Instance

### Create a Python virtual environment:

```bash
python3 -m venv myvenv
```

### Activate the virtual environment for local development:

```bash
source myvenv/bin/activate
```

### Run the tests:

```bash
python runtests.py
```
### Check the django test app:

```bash
python manage.py check
```


## Build the docs, within the docs directory:

```bash
make html
```
