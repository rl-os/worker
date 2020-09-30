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
    _maxCombo: int

    # beatmap stats
    _count_total: int
    _ar: float
    _od: float

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
        raw_aim: float = .1

        # TODO: touch device

        self.aim = math.pow(
            5.0 * max(1.0, raw_aim / 0.0675) - 4.0, 3.0
        ) / 100000.0

        total_hits = self.total_hits

        length_bonus = .95 + .4 * min(1.0, total_hits / 2000.0) + (
            math.log10(total_hits / 2000.0) * 0.5
            if total_hits > 2000
            else .0
        )

        self.aim *= length_bonus
        self.aim *= math.pow(.97, self._numMiss)

        if self._maxCombo > 0:
            self.aim *= min(
                (math.pow(self._maxCombo, .8) / math.pow(self._count_total, .8)),
                1.0
            )

        approach_rate_factor = 1.0
        if self._ar > 10.33:
            approach_rate_factor += .3 * (self._ar - 10.33)
        else:
            approach_rate_factor += .01 * (8.0 - self._ar)

        self.aim *= approach_rate_factor

        if Mod.Easy in self._mods:
            self.aim *= 1.0 + .04 * (12.0 - self._ar)

        if Mod.Flashlight in self._mods:
            pass
            # TODO: this
            # _aimValue *= 1.0f + 0.35f * std::min(1.0f, static_cast<f32>(numTotalHits) / 200.0f) +
            #          	(numTotalHits > 200 ? 0.3f * std::min(1.0f, static_cast<f32>(numTotalHits - 200) / 300.0f) +
            #          	(numTotalHits > 500 ? static_cast<f32>(numTotalHits - 500) / 1200.0f : 0.0f) : 0.0f);

        # scale the aim value with accuracy _slightly_
        self.aim *= .5 + self.acc / 2.0
        # it is important to also consider accuracy difficulty when doing that
        self.aim *= .98 + (math.pow(self._od, 2) / 2500)
