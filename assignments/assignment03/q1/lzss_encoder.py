#!/usr/bin/env python3

"""
FIT3155 - Assignment 3

Semester 2 2019

Dylan Pinn 24160547


Q1: LZSS Encoder
"""

import sys

import elias_encoder
import huffman_coding
import lzss_encoder_class


class Encoder:
    def __init__(self, string: str, window_size: int, buffer_size: int):
        self.string = string
        self.window_size = window_size
        self.buffer_size = buffer_size
        self.huffman_values = huffman_coding.encoded_values(string)[0]

    def encode(self):
        """Combine the header and data."""
        result = self.encode_header()
        result += self.encode_data()
        return result

    def encode_header(self) -> str:
        """
        Encode string into Header.
        - Encode using variable-length Elias, the no of unique ASCII characters.
        - For each unique char
        -- Encode using fixed-length 8-bit ASCII code the unique char
        -- Encode using variable-length Elias code the length of the Huffman code
           assigned to that unique char
        """
        result = ""

        unique_chars = huffman_coding.unique_chars(self.string)
        unique_chars_list = list(unique_chars)
        unique_chars_list.sort()
        no_of_unique = len(unique_chars_list)

        result += elias_encoder.encode_single_value(no_of_unique)

        for char in unique_chars_list:
            ascii_8_bit = self.convert_to_8_bit_ascii(char)
            huffman_code = self.huffman_values[char]
            encoded_huffman_len = elias_encoder.encode_single_value(
                len(huffman_code)
            )

            result += ascii_8_bit
            result += encoded_huffman_len
            result += huffman_code

        return result

    def encode_data(self) -> str:
        result = ""
        lzss_encoding = lzss_encoder_class.LZSSEncoder(
            self.string, self.window_size, self.buffer_size
        ).encode()
        result += elias_encoder.encode_single_value(len(lzss_encoding))

        for encoding in lzss_encoding:
            if encoding[0] == 0:
                result += "0"
                result += elias_encoder.encode_single_value(
                    encoding[1]  # type: ignore
                )
                result += elias_encoder.encode_single_value(
                    encoding[2]  # type: ignore
                )
            else:
                result += "1"
                huffman_code = self.huffman_values[encoding[1]]  # type: ignore
                result += huffman_code
        return result

    @staticmethod
    def convert_to_8_bit_ascii(char: str) -> str:
        return "{0:0=8d}".format(int(bin(ord(char))[2:]))


if __name__ == "__main__":
    print("aaa")
    input_text = open(sys.argv[1], "r")
    w_size = sys.argv[2]
    b_size = sys.argv[3]
    print(w_size)
    print(b_size)
