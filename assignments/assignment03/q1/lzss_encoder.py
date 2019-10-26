#!/usr/bin/env python3

"""
FIT3155 - Assignment 3

Semester 2 2019

Dylan Pinn 24160547


Q1: LZSS Encoder
"""

from . import elias_encoder, huffman_coding


def encode_header(string: str, window_size: int, buffer_size: int) -> str:
    """
    Encode string into Header.
    - Encode using variable-length Elias, the no of unique ASCII characters.
    - For each unique char
    -- Encode using fixed-length 8-bit ASCII code the unique char
    -- Encode using variable-length Elias code the length of the Huffman code
       assigned to that unique char
    """
    result = ""

    unique_chars = huffman_coding.unique_chars(string)
    unique_chars_list = list(unique_chars)
    unique_chars_list.sort()
    no_of_unique = len(unique_chars_list)

    huffman_values = huffman_coding.encoded_values(string)[0]
    print(huffman_values)

    result += elias_encoder.encode_single_value(no_of_unique)

    for char in unique_chars_list:
        ascii_8_bit = convert_to_8_bit_ascii(char)
        huffman_code = huffman_values[char]
        encoded_huffman_len = elias_encoder.encode_single_value(
            len(huffman_code)
        )

        result += ascii_8_bit
        result += encoded_huffman_len
        result += huffman_code
        print(ascii_8_bit)
        print(encoded_huffman_len)
        print(huffman_code)

    return result


def convert_to_8_bit_ascii(char: str) -> str:
    return "{0:0=8d}".format(int(bin(ord(char))[2:]))
