from typing import List, Tuple


class LZ77Decoder:
    def __init__(
        self,
        code: List[Tuple[int, int, str]],
        window_size: int,
        buffer_size: int,
    ):
        self.code = code
        self.window_size = window_size
        self.buffer_size = buffer_size

    def decode(self) -> str:
        result = ""

        for code in self.code:
            offset = code[0]
            length = code[1]
            next_char = code[2]
            index = len(result)
            if length == 0 and offset == 0:
                result += next_char
                continue
            substring = result[index - offset : index]
            substring = self.repeat_to_length(substring, length)
            result += substring
            result += next_char

        return result

    @staticmethod
    def repeat_to_length(string_to_expand: str, length: int) -> str:
        return (string_to_expand * (int(length / len(string_to_expand)) + 1))[
            :length
        ]
