import lzma
import struct
import datetime

from src.replay.parser import Parser
from src.models.replay import Replay
from src.models.replay_event import ReplayEvent
from src.models.replay_mods import GameMode, Mod


class ReplayParser:
    @staticmethod
    def from_bytes(data: bytes) -> Replay:
        """
        Парсит реплей и возвращяет в виде `Replay`
        :param data: бинарный файл osr
        :return: реплей
        """
        replay = Replay()

        replay = ReplayParser.parse_game_mode_and_version(replay, data)
        replay = ReplayParser.parse_beatmap_hash(replay, data)
        replay = ReplayParser.parse_player_name(replay, data)
        replay = ReplayParser.parse_replay_hash(replay, data)
        replay = ReplayParser.parse_score_stats(replay, data)
        replay = ReplayParser.parse_life_bar_graph(replay, data)
        replay = ReplayParser.parse_timestamp_and_replay_length(replay, data)

        return ReplayParser.parse_play_data(replay, data)

    @staticmethod
    def parse_game_mode_and_version(r: Replay, replay_data: bytes) -> Replay:
        format_specifier = "<bi"

        data = struct.unpack_from(format_specifier, replay_data, r.offset)

        r.offset += struct.calcsize(format_specifier)
        r.game_mode = GameMode(data[0])
        r.game_version = data[1]

        return r

    @staticmethod
    def parse_beatmap_hash(r: Replay, replay_data: bytes) -> Replay:
        (r.beatmap_hash, r.offset) = Parser.parse_string(r.offset, replay_data)

        return r

    @staticmethod
    def parse_player_name(r: Replay, replay_data: bytes) -> Replay:
        (r.player_name, r.offset) = Parser.parse_string(r.offset, replay_data)

        return r

    @staticmethod
    def parse_replay_hash(r: Replay, replay_data: bytes) -> Replay:
        (r.replay_hash, r.offset) = Parser.parse_string(r.offset, replay_data)

        return r

    @staticmethod
    def parse_score_stats(r: Replay, replay_data: bytes) -> Replay:
        format_specifier = "<hhhhhhih?i"
        data = struct.unpack_from(format_specifier, replay_data, r.offset)

        # распаковываем статистику по реплею
        r.number_300s, r.number_100s,\
            r.number_50s, r.gekis,\
            r.katus, r.misses, r.score,\
            r.max_combo, r.is_perfect_combo,\
            r.mod_combination = data

        r.mods = set(Mod(mod_val) for mod_val in Parser.bits(r.mod_combination))
        r.offset += struct.calcsize(format_specifier)

        return r

    @staticmethod
    def parse_life_bar_graph(r: Replay, replay_data: bytes):
        (r.life_bar_graph, r.offset) = Parser.parse_string(r.offset, replay_data)

        return r

    @staticmethod
    def parse_timestamp_and_replay_length(r: Replay, replay_data: bytes) -> Replay:
        format_specifier = "<qi"
        (t, r.replay_length) = struct.unpack_from(format_specifier, replay_data, r.offset)

        r.timestamp = datetime.datetime.min + datetime.timedelta(microseconds=t / 10)
        r.offset += struct.calcsize(format_specifier)

        return r

    @staticmethod
    def parse_play_data(r: Replay, replay_data) -> Replay:
        offset_end = r.offset + r.replay_length

        if r.game_mode != GameMode.Standard:
            r.play_data = None
        else:
            dec = lzma.decompress(
                replay_data[r.offset:offset_end],
                format=lzma.FORMAT_AUTO
            )

            string = dec.decode('ascii')[:-1]
            events = [event.split('|') for event in string.split(',')]

            r.play_data = [
                ReplayEvent(
                    time_since_previous_action=int(event[0]),
                    x=float(event[1]),
                    y=float(event[2]),
                    keys_pressed=int(event[3])
                )
                for event in events
            ]

        r.offset = offset_end

        return r
