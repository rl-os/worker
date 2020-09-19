from src.models.user import UserShort
from src.utils import nested_dataclass


@nested_dataclass
class NewReplayRequest:
    replay_id: int
    user: UserShort
    bucket: str
    key: str
