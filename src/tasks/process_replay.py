from celery.task import Task
from celery.utils.log import get_task_logger

from src.entrypoint import entrypoint
from src.models.requsets.new_replay import NewReplayRequest


log = get_task_logger(__name__)


@entrypoint.register_task
class ProcessReplay(Task):
    name = 'rl.worker.process_replay'

    def run(self, *args, **kwargs):
        """
        Вызывается celery, парсит полученый json в dataclass и запускает обработку реплея
        """
        log.info("exec")

    def _process(self, req: NewReplayRequest) -> None:
        replay_data = self._load_replay(req.bucket, req.key)
        # todo: calculate pp and accuracy
        # todo: anticheat validation (secret code?)
        # todo: check achievements
        # todo: upload result

        log.debug(replay_data)

    def _load_replay(self, bucket: str, key: str):
        pass
