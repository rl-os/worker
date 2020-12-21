import oppai

from src.models.replay import Replay
from src.models.score import Score


class Performance:
    @staticmethod
    def process(replay: Replay, beatmap_data: bytes) -> Score:
        ez = oppai.ezpp_new()

        try:
            oppai.ezpp_set_autocalc(ez, 1)

            oppai.ezpp_data(ez, beatmap_data.decode(), len(beatmap_data))

            mods = 0
            for mod in replay.mods:
                mods |= mod.value

            oppai.ezpp_set_mods(ez, mods)
            oppai.ezpp_set_combo(ez, replay.max_combo)
            oppai.ezpp_set_nmiss(ez, replay.misses)
            oppai.ezpp_set_accuracy(ez, replay.number_100s, replay.number_50s)

            score = Score(
                replay=replay,
                accuracy=oppai.ezpp_accuracy_percent(ez),
                pp=oppai.ezpp_pp(ez),
            )
        except Exception as e:
            raise e
        finally:
            oppai.ezpp_free(ez)

        return score
