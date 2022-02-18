# Contributing to django-directed

For development and testing, you can run a Postgres database in Docker Compose. This guide assumes you already have Docker and Docker Compose installed.

Build the Docker Compose container for Postgres:

    docker-compose -f dev.yml up -d --no-deps --force-recreate --build postgres

To check the status of the database container:

    docker ps

Database connection details:

    HOST = postgres
    PORT = 9932
    USER = docker
    PASSWORD = docker
    DB = postgres

If you need to remove the container:

    docker-compose -f dev.yml down --rmi all --remove-orphans -v

Create a Python virtual environment:

    python3 -m venv myvenv

Activate the virtual environment:

    source myvenv/bin/activate

Run the tests:

    python runtests.py

Run the django test app:

    python manage.py check

To build the docs, within the docs directory:

    make html
