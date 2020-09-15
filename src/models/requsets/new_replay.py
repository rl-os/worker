from dataclasses import dataclass

from src.models.user import UserShort


@dataclass
class NewReplayRequest:
    replay_id: int
    user: UserShort
    bucket: str
    key: str
