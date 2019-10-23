"""
FIT3155 Assigment 3

Task 1
"""

from . import elias_encoder
from . import huffman_coding


class Encoder:
    def __init__(self, code: str):
        self.code = code
        self.huffman_values = huffman_coding.encoded_values(code)[0]

    def encode_header(self) -> str:
        header = ""
        unique_chars = huffman_coding.unique_chars(self.code)
        # Encode the number of unique values in the input txt
        header += elias_encoder.encode_single_value(len(unique_chars))
        for val in sorted(unique_chars):
            # Encode the 8-bit ASCII code
            header += self.convert_to_8_bit_ascii(val)
            huff_code = self.huffman_values[val]
            # Encode the length of the Huffman code
            header += elias_encoder.encode_single_value(len(huff_code))
            # Add the Huffman code
            header += huff_code

        return header

    @staticmethod
    def convert_to_8_bit_ascii(char: str) -> str:
        return "{0:0=8d}".format(int(bin(ord(char))[2:]))
