from src.models.beatmap import Beatmap
from src.models.replay import Replay


class Performance:
    def __init__(self, beatmap: Beatmap, replay: Replay):
        self.beatmap = beatmap
        self.replay = replay

    def process(self):
        pass


class ManiaPerformance:
    def __init__(self):
        pass
