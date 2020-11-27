# RL Worker
High performance [osu!](https://osu.ppy.sh) score server which isn't based on [Ripple](https://ripple.moe/) stack.

![](https://i.imgur.com/W4QBLfs.png)

## Features
 - Score submission
 - Supports any osu! version and all game modes (standard, taiko, catch, mania) 
 - Replay s3 ~~or local~~ storage
 - [Poetry](https://python-poetry.org/)
 - Based on [Celery](https://github.com/celery/celery) with RabbitMQ queues


## Getting Started

```sh
# install poetry (osx / linux / bash-on-windows)
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
# powershell (windows only)
$ (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python

# setup all dependencies
$ poetry install

$ cp config.example.yaml config.yaml
$ vim config.yaml

# starting worker
$ poetry run worker
```
