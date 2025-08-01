# FastAPI Template
Template repo for building FastAPI applications

## Requirements
* Poetry >= 1.8.2 
* Python >= 3.12

## Use
* Run `poetry install` to install all dependencies as specified in `pyproject.yaml`.
* Run `poetry run dev` to run a local server for development.
* Run `pytest` to execute unit tests.

## Modifications
Overview of reasonable next steps to take from this starting point:

### CI/CD 
WIP will be included here

### Security
* Basic JWT processing and authentication for external SSO
* Custom password hashing / verification

### SQL
* DB driver
* New directory app/models
  * -> add new models here as appropriate
* Create an interface / connection logic at app/core/db.py

### Generic Improvements
* Augment context.py and config.py as necessary

## File Structure
```
fastapi_app/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── context.py
│   │   └── logging.py
│   ├── scripts/
│   │   └── dev_server.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── pyproject.toml
├── README.md
└── .env
```
