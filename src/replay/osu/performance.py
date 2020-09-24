from typing import List

import math

from src.models.beatmap import Beatmap
from src.models.replay import Replay
from src.models.replay_mods import Mod


class OsuPerformance:
    # TODO: optimisation @property

    # computed stats
    pp: float
    total: float
    aim: float
    speed: float
    acc: float

    # input data
    _mods: List[Mod]
    _num50: int
    _num100: int
    _num300: int
    _numMiss: int

    def __init__(self, beatmap: Beatmap, replay: Replay):
        pass

    @property
    def total_hits(self) -> int:
        return self._num50 + self._num100 + self._num300 + self._numMiss

    @property
    def total_successful_hits(self) -> int:
        return self._num50 + self._num100 + self._num300

    def compute_accuracy(self):
        if self.total_hits is 0:
            return 0

        self.acc = (self._num50 * 50 + self._num100 * 100 + self._num300 * 300) / (self.total_hits * 300)

    def compute_total_value(self):
        if (Mod.Relax, Mod.Autoplay, Mod.Autopilot) in self._mods:
            self.total = .0
            return

        # custom multipliers for NoFail and SpunOut.
        # this is being adjusted to keep the final pp
        # value scaled around what it used to be when changing things
        multiplier: float = 1.12

        if Mod.NoFail in self._mods:
            multiplier *= 0.9

        if Mod.SpunOut in self._mods:
            multiplier *= 0.95

        self.total = math.pow(
            math.pow(self.aim, 1.1) +
            math.pow(self.speed, 1.1) +
            math.pow(self.acc, 1.1),
            1.0 / 1.1
        ) * multiplier

    def compute_aim(self):
        # TODO: fixme
        raw_aim = .1

        # TODO: touch device

        aim_value = math.pow(
            5.0 * max(1.0, raw_aim / 0.0675) - 4.0, 3.0
        ) / 100000.0

        total_hits = self.total_hits

