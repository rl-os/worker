from typing import Any, Dict, List

import boto3
from celery.task import Task
from celery.utils.log import get_task_logger

import src.client
from src.client.rest import ApiException

from src.config import config
from src.entrypoint import entrypoint
from src.models.score import ParsedScore
from src.models.requsets.new_replay import NewReplayRequest

log = get_task_logger(__name__)

s3 = boto3.client(
    's3',
    endpoint_url=config.s3.endpoint_url,
    region_name='ru-1a',
    aws_access_key_id=config.s3.access_key_id,
    aws_secret_access_key=config.s3.secret_access_key,
)

configuration = src.client.Configuration()
configuration.host = config.rl.api_url
configuration.api_key = config.rl.access_token

api_instance = src.client.InternalApi(src.client.ApiClient(configuration))


@entrypoint.register_task
class ProcessReplay(Task):
    name = 'rl.worker.process_replay'

    def run(self, data: Dict[str, Any]):
        """
        Вызывается celery, парсит полученый json в dataclass и запускает обработку реплея
        """

        log.debug('parse request')
        req = NewReplayRequest(**data)

        log.debug('process replay from request data')
        return self._process(req)

    def _process(self, req: NewReplayRequest) -> None:
        replay_file = self._load_replay(req.bucket, req.key)

        parsed = self._parse_replay(replay_file)

        score = self._calculate(parsed)

        is_cheat = self._anticheat(parsed, score)

        if is_cheat is True:
            log.warn(f'found cheater with id={req.user.id}')
            # todo: this
        else:
            log.debug('save results')
            self._send_score(req, parsed)

    def _load_replay(self, bucket: str, key: str) -> bytearray:
        log.debug('loading replay from s3 bucket')

        return bytearray()

    def _parse_replay(self, replay_data: bytearray) -> ParsedScore:
        pass

    def _calculate(self, parsed: ParsedScore) -> Any:
        pass

    def _anticheat(self, parsed: ParsedScore, score) -> bool:
        pass

    def _send_score(self, req: NewReplayRequest, parsed: ParsedScore):
        body = src.client.UpdateScoreRequest(
            replay_id=req.replay_id,
            user_id=req.user.id,
            parsed=parsed,
        )

        try:
            # Score submission
            api_instance.api_internal_scores_submit_post(body)
        except ApiException as e:
            self.retry(
                max_retries=3,
                exc=e,
            )


if __name__ == '__main__':
    # noinspection PyCallByClass
    ProcessReplay.apply_async(kwargs={
        'data': {
            "replay_id": 1,
            "bucket": "replays",
            "key": "replay-1-somedandomuuid.osr",
            "user": {}
        }
    })

