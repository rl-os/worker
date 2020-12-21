from typing import List

from datetime import datetime
from pydantic import BaseModel

from src.models.replay_event import ReplayEvent
from src.models.replay_mods import GameMode, Mod


class Replay(BaseModel):
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
    mods: List[Mod] = []
    life_bar_graph: str = None
    timestamp: datetime = None
    replay_length: int = 0
    play_data: List[ReplayEvent] = []
