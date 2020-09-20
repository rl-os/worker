from typing import List, Set

import datetime
from dataclasses import field

from src.models.replay_event import ReplayEvent
from src.utils import nested_dataclass
from src.models.replay_mods import GameMode, Mod


@nested_dataclass
class Replay:
    offset: int = 0
    game_mode: GameMode = None
    game_version: int = None
    beatmap_hash: str = None
    player_name: str = None
    replay_hash: str = None
    number_300s: int = None
    number_100s: int = None
    number_50s: int = None
    gekis: int = None
    katus: int = None
    misses: int = None
    score: int = None
    max_combo: int = None
    is_perfect_combo: bool = None
    mod_combination: int = None
    mods: List[Mod] = field(default_factory=list)
    life_bar_graph: str = None
    timestamp: datetime.datetime = None
    replay_length: int = 0
    play_data: List[ReplayEvent] = None
