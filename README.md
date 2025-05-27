# django-deepface-demo

This repository demonstrates the django-deepface library, which integrates the deepface library into a Django project. It provides a lightweight test harness for django-deepface, allowing you to run and test the integration in a controlled environment.

## ensuring Python 3.11 - don't use 3.12 or 3.13 - tensorflow issues on M3

  ```bash
  brew install python@3.11
  python3.11 -m venv .venv
  pip install uv
  uv pip install -r requirements.txt 
  
  ```

 
## Setup

## pg
```bash
PGPASSWORD=postgres psql -h localhost -p 5432 -U postgres -d vectordb
psql (14.16 (Homebrew), server 17.4 (Debian 17.4-1.pgdg120+2))
WARNING: psql major version 14, server major version 17.
                                                             ^
vectordb=# create extension if not exists vector;
CREATE EXTENSION
vectordb=# CREATE table identities (ID INT primary key, IMG_PATH varchar(180), embedding vector(128));
CREATE TABLE

```

# Running Tests

You can run the django_deepface test suite from this project. The test harness is set up so that all upstream tests run in your environment, using your settings and database.

- To run all tests (your own and django_deepface's):
  ```bash
  make test-all
  ```

- To run only the django_deepface suite:
  ```bash
  make test-specific test="dftest/tests/test_deepface_suite.py -v"
  ```

All required fixtures and test images are included, so the upstream suite will run and pass as part of your workflow.