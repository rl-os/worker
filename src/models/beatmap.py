from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime


class Failtimes(BaseModel):
    fail: Optional[List[int]]
    exit: Optional[List[int]]


class Beatmap(BaseModel):
    difficulty_rating: float
    id: int
    mode: str
    version: str
    accuracy: int
    bpm: int
    ar: float
    cs: int
    drain: int
    beatmapset_id: int
    convert: bool
    count_circles: int
    count_sliders: int
    count_spinners: int
    count_total: int
    deleted_at: Optional[datetime] = None
    hit_length: int
    is_scoreable: bool
    last_updated: datetime
    mode_int: int
    passcount: int
    playcount: int
    ranked: int
    status: str
    total_length: int
    url: str
    failtimes: Optional[Failtimes] = None
    max_combo: Optional[int] = None
