from celery.bin import worker

# noinspection PyUnresolvedReferences
from src.entrypoint import entrypoint
# noinspection PyUnresolvedReferences
from src.tasks import *


def run():
    app = worker.worker(app=entrypoint)

    options = {
        'broker': 'amqp://guest:guest@localhost:5672//',
        'loglevel': 'INFO',
        'traceback': True,
        'beat': True
    }

    app.run(**options)


if __name__ == '__main__':
    run()
