from pydantic import BaseModel
from src.models.replay import Replay
from src.models.user import UserShort


class Score(BaseModel):
    replay: Replay
    accuracy: float
    pp: float


class UpdateScore(BaseModel):
    id: int
    user: UserShort
    parsed: Score
