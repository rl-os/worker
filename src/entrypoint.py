import os

import celery
from typing import Union

from src.config import config


class EntryPoint(celery.Celery):
    TASK_ROUTES = {
        'rl.worker.process_replay': {
            'queue': 'rl.worker.process_replay',
            'routing_key': 'rl.worker.process_replay',
            'prefetch_count': 1,
        },
    }

    def __init__(self):
        self.read_config(os.getenv("CONFIG_PATH") or "config.yaml")

        super().__init__(
            'rl-worker',
            broker=config.amqp.url,
        )
        self.conf.update(
            # настройки для того что бы таски писались в rabbitmq в виде json
            # а не в виде обьектов celery
            CELERY_TASK_SERIALIZER='json',
            CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
            CELERY_RESULT_SERIALIZER='json',
            CELERY_ENABLE_UTC=True,
            CELERY_TASK_PROTOCOL=1,

            # WARNING: отключаем сохранение статуса задачи
            # позволяет повысить производительность тк не пишется в sqltite3 и другие статусы задач
            CELERY_IGNORE_RESULT=True,

            # WARNING: !!!
            # нужно для каждой задачи указать свою очередь
            CELERY_ROUTES=self.TASK_ROUTES,
        )

        self.on_after_configure.connect(self.postfork)

    def read_config(self, path: Union[str, None]):
        """
        Загружает конфиг и наполняет с использованием переменных окружения
        :param path: Путь до файла конфигурации
        :return:
        """
        if path is not None:
            config.update_from_file(
                path=path,
                allow_missing_keys=True
            )

        config.update_from_env(
            env_prefix='RL',
            delimiter='__'
        )

    def postfork(self, sender, **kwargs):
        """
        Запускается после того как celery форкнет наш воркер
        """
        pass


entrypoint = EntryPoint()
