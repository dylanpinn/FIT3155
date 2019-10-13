"""
FIT3155 - Assignment 3

Semester 2 2019

Dylan Pinn 24160547
"""

import elias_encoder
import huffman_coding


def encoder(code: str, window_size: int, buffer_size: int):
    pass


def encode_header(code):
    header = ""
    unique_chars = huffman_coding.unique_chars(code)
    # Encode the number of unique values in the input txt
    header += elias_encoder.encode_single_value(len(unique_chars))
    huffman_values = huffman_coding.encoded_values(code)[0]
    for val in unique_chars:
        # Encode the 8-bit ASCII code
        header += convert_to_8_bit_acii(val)
        huff_code = huffman_values[val]
        # Encode the length of the Huffman code
        header += elias_encoder.encode_single_value(len(huff_code))
        # Add the Huffman code
        header += huff_code

    return header


def convert_to_8_bit_acii(char: str) -> str:
    return "{0:0=8d}".format(int(bin(ord(char))[2:]))
