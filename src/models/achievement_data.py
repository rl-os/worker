from pydantic import BaseModel


class AchievementData(BaseModel):
    id: str
    name: str
    description: str
    icon: str

    index: int
    mode: str
