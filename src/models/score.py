from typing import Union

from src.models.replay import Replay
from src.utils import nested_dataclass
from src.models.user import UserShort


@nested_dataclass
class Score:
    replay: Replay
    accuracy: float
    pp: float


@nested_dataclass
class UpdateScore:
    id: int
    user: UserShort
    parsed: Score
