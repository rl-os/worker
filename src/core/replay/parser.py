from typing import Tuple

BYTE = 1
SHORT = 2
INT = 4
LONG = 8


class Parser:
    @staticmethod
    def bits(n: int):
        """
        Generator yielding value of each bit in an integer if it's set + value
        of LSB no matter what .
        """
        if n == 0:
            yield 0
        while n:
            b = n & (~n + 1)
            yield b
            n ^= b

    @staticmethod
    def decode(offset: int, data: bytes) -> Tuple[int, int]:
        result = 0
        shift = 0
        while True:
            byte = data[offset]
            offset += 1
            result = result | ((byte & 0b01111111) << shift)
            if (byte & 0b10000000) == 0x00:
                break
            shift += 7

        return result, offset

    @staticmethod
    def parse_int(bytestring):
        return int.from_bytes(bytestring, byteorder='little')

    @staticmethod
    def parse_string(offset: int, replay_data: bytes) -> Tuple[str, int]:
        """
        Парсит из бинарных данных строчку по ее оффсету и возвращяет ее вместе с новым оффсетом
        :param offset:
        :param replay_data:
        :return:
        """
        if replay_data[offset] == 0x00:
            offset += BYTE
        elif replay_data[offset] == 0x0b:
            offset += BYTE
            string_length, offset = Parser.decode(offset, replay_data)
            offset_end = offset + string_length
            string = replay_data[offset:offset_end].decode("utf-8")
            offset = offset_end

            return string, offset
        else:
            raise Exception("Invalid replay")
