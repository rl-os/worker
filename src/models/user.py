from typing import List, Any, Union

from datetime import datetime
from pydantic import BaseModel


class Country(BaseModel):
    code: str
    name: str


class Cover(BaseModel):
    custom_url: str
    url: str
    id: Union[int, None]


class UserShort(BaseModel):
    avatar_url: str
    country_code: str
    default_group: str
    id: int
    is_active: bool
    is_bot: bool
    is_online: bool
    is_supporter: bool
    last_visit: datetime
    pm_friends_only: bool
    profile_colour: Union[str, None]
    username: str
    country: Country
    cover: Cover
    current_mode_rank: int
    groups: List[Any]
    support_level: int
