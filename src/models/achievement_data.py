from src.utils import nested_dataclass


@nested_dataclass
class AchievementData:
    id: str
    name: str
    description: str
    icon: str

    index: int
    mode: str
