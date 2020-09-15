from typing import List, Union

from dataclasses import dataclass

from src.models.user import UserShort


@dataclass
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


@dataclass
class UpdateScore:
    id: int
    user: UserShort
    parsed: ParsedScore
