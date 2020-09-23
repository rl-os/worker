from src.models.beatmap import Beatmap
from src.models.replay import Replay


class Performance:
    def __init__(self, beatmap: Beatmap, replay: Replay):
        self.beatmap = beatmap
        self.replay = replay

    def process(self):
        pass


class OsuPerformance:
    # TODO: optimisation @property

    pp: float

    _num50: int
    _num100: int
    _num300: int
    _numMiss: int

    def __init__(self):
        pass

    @property
    def total_hits(self) -> int:
        return self._num50 + self._num100 + self._num300 + self._numMiss

    @property
    def accuracy(self):
        if self.total_hits is 0:
            return 0

        return (self._num50 * 50 + self._num100 * 100 + self._num300 * 300) / (self.total_hits * 300)


class ManiaPerformance:
    def __init__(self):
        pass
