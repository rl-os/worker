from typing import Any, Dict, List

import boto3
from celery.task import Task
from celery.utils.log import get_task_logger

import src.client
from src.client.rest import ApiException

from src.config import config
from src.entrypoint import entrypoint

from src.replay import ReplayParser
from src.models.score import Score
from src.models.replay import Replay
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

    acks_late = True
    max_retries = None
    default_retry_delay = 15 * 60  # 15 min

    def run(self, data: Dict[str, Any]):
        """
        Вызывается celery, парсит полученый json в dataclass и запускает обработку реплея
        """

        log.debug('parse request')

        req = NewReplayRequest(**data)

        log.debug('process replay from request data')
        try:
            return self._process(req)
        except Exception as exc:
            raise self.retry(exc=exc)

    def _process(self, req: NewReplayRequest) -> None:
        replay_file = self._load_replay(req.bucket, req.key)

        parsed = self._parse_replay(replay_file)

        score = self._calculate(parsed)

        is_cheat = self._anticheat(parsed, score)

        if is_cheat is True:
            log.warn(f'found cheater with id={req.user.id}')
            # todo: this
        else:
            log.info('save results')
            self._send_score(req, parsed)

    def _load_replay(self, bucket: str, key: str) -> bytes:
        log.info('loading replay from s3 bucket')

        get_object_response = s3.get_object(Bucket=bucket, Key=key)
        return get_object_response['Body'].read()

    def _parse_replay(self, replay_data: bytes) -> Replay:
        return ReplayParser.from_bytes(replay_data)

    def _calculate(self, parsed: Replay) -> Score:
        pass

    def _anticheat(self, parsed: Replay, score) -> bool:
        pass

    def _send_score(self, req: NewReplayRequest, parsed: Replay):
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
            "key": "replay-3af6b346-a185-46b0-af70-b5115f0f3507.osr",
            "user": {
                "avatar_url": "https://301222.selcdn.ru/akasi/avatars/1.png",
                "country_code": "RU",
                "default_group": "default",
                "id": 100,
                "is_active": True,
                "is_bot": False,
                "is_online": True,
                "is_supporter": True,
                "last_visit": "2020-09-20T14:41:13+00:00",
                "pm_friends_only": True,
                "profile_colour": None,
                "username": "deissh",
                "country": {
                    "code": "RU",
                    "name": "Russian Federation"
                },
                "cover": {
                    "custom_url": "https://301222.selcdn.ru/akasi/bg/1.jpg",
                    "url": "https://301222.selcdn.ru/akasi/bg/1.jpg",
                    "id": None
                },
                "current_mode_rank": 1,
                "groups": [],
                "support_level": 2
            }
        }
    })

