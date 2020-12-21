from pydantic import BaseModel

from src.models.user import UserShort
from src.models.beatmap import Beatmap


class NewReplayRequest(BaseModel):
    replay_id: int
    key: str
    user: UserShort
    beatmap: Beatmap
