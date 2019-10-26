"""
FIT3155 - Assignment 3

Semester 2 2019

Dylan Pinn 24160547


LZSS Decoder
"""
from typing import List, Tuple, Union

Format0 = Tuple[int, int, int]
Format1 = Tuple[int, str]
EncodingType = Union[Format0, Format1]


class LZSSDecoder:
    def __init__(
        self, code: List[EncodingType], window_size: int, buffer_size: int
    ):
        self.code = code
        self.window_size = window_size
        self.buffer_size = buffer_size

    def decode(self) -> str:
        result = ""

        for code in self.code:
            format_bit = code[0]

            if format_bit == 1:
                next_char = code[1]
                result += next_char  # type: ignore
                continue
            elif format_bit == 0:
                offset = code[1]
                length = code[2]  # type: ignore
                index = len(result)
                substring = result[index - offset : index]  # type: ignore
                substring = self.repeat_to_length(substring, length)
                result += substring
            else:
                raise Exception

        return result

    @staticmethod
    def repeat_to_length(string_to_expand: str, length: int) -> str:
        return (string_to_expand * (int(length / len(string_to_expand)) + 1))[
            :length
        ]
