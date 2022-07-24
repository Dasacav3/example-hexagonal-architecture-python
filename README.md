# Example of Hexagonal Architecture With Python

This is an example of a hexagonal architecture with Python. The architecture is based on the experience and knowledge, I have implemented dependency injection using the library dependency-injector.

## DynamoDB table schema

The table must have the following attributes:

- partition key: model
- sort key: id

Data Example

```
{
    "id": "1",
    "model": "user",
    "name": "name1",
    "email": "email@gmail.com",
    "password": "password",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z"
}
```


## How to run without docker

You must create a .env file in the root directory of the project and then run the following commands:

```bash
$ pip install -r requirements.txt
$ python -B app.py
```

## How to run with docker

You must create a .env file in the root directory of the project and then run the following commands:

```bash
$ docker-compose up --build
```