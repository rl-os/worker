from typing import List

from src.core.base_achievement import BaseAchievement
from src.models.score import Score
from src.models.achievement_data import AchievementData


class Combo(BaseAchievement):
    base = {
        "id": "osu-combo-{mode}-{index}",
        "name": "{index} Combo (osu!{mode})",
        "description": "{index} big ones! You're moving up in the world!",
        "icon": "osu-combo-{index}"
    }

    keys = {
        "index": [500, 750, 1000, 2000],
        "mode": ["std", "taiko", "ctb", "mania"]
    }

    struct = {
        "index": 1,
        "mode": 4
    }

    achievements: List[AchievementData] = []

    def __init__(self):
        super().__init__()

    def handle(self, score: Score) -> List[str]:
        achievement_ids = []

        for ach in self.achievements:
            if ach.index > score.replay.max_combo or ach.mode is not score.replay.mods:
                continue

            achievement_ids.append(ach.id)

        return achievement_ids
