# RL Worker
High performance score server which doesn't based on ripple's stack

![](https://i.imgur.com/W4QBLfs.png)

## Features
 - Score submission
 - Support any osu! version and game mod (mania, catch, fruit) 
 - Replay s3 ~~or local~~ storage
 - [Poetry](https://python-poetry.org/)
 - Based on [Celery](https://github.com/celery/celery) with RabbitMQ queues


## Getting Started

```bash
# osx / linux / bashonwindows install poetry
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
# windows powershell
$ (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python

# setup all dependencies
$ poetry install

$ cp config.example.yaml config.yaml
$ vim config.yaml

# starting worker
$ poetry run worker
```