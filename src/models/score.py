from typing import List, Union

from src.utils import nested_dataclass
from src.models.user import UserShort


@nested_dataclass
class ParsedScore:
    mode: str  # osu, taiko, catch, mania
    enabled_mods: List[str]
    count50: int
    count100: int
    count300: int
    countgeki: int
    countkatu: int
    countmiss: int
    maxcombo: int
    passed: int
    perfect: int
    score: int
    frame: int
    playtime: int

    accuracy: Union[float, None] = None
    pp: Union[float, None] = None


@nested_dataclass
class UpdateScore:
    id: int
    user: UserShort
    parsed: ParsedScore
