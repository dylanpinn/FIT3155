#!/usr/bin/env python3

"""
FIT3155 - Assignment 3

Semester 2 2019

Dylan Pinn 24160547


Q1: LZSS Decoder
"""

from typing import Dict, List, Tuple, Union

from . import elias_decoder, elias_encoder, lzss_decoder_class

Format0 = Tuple[int, int, int]
Format1 = Tuple[int, str]
EncodingType = Union[Format0, Format1]


class Decoder:
    def __init__(self, code: str):
        self.code = code
        self.huffman_coding: Dict[str, str] = {}

    def decode(self) -> str:
        """Decode the LZSS Encoded code."""
        code = self.code
        # Decode Header

        # Decode the number of unique ASCII characters.
        no_of_unique = elias_decoder.decode_single_value(code)
        code_to_remove = elias_encoder.encode_single_value(no_of_unique)
        code = code[len(code_to_remove) :]
        for i in range(no_of_unique):
            # Decode the fixed-length 8-bit ASCII code of the unique char.
            unique_char_code = code[0:8]
            unique_char = chr(int(unique_char_code, 2))
            code = code[8:]

            # Decode the length of the variable-length Elias code of the
            # length of the Huffman code used for the unique char.
            length_of_huffman = elias_decoder.decode_single_value(code)
            code_to_remove = elias_encoder.encode_single_value(
                length_of_huffman
            )
            code = code[len(code_to_remove) :]

            # Retrieve the Huffman codeword for that unique char.
            huffman_code = code[0:length_of_huffman]
            code = code[length_of_huffman:]

            self.huffman_coding[unique_char] = huffman_code

        # Decode Data
        no_of_lzss_encodings = elias_decoder.decode_single_value(code)
        code_to_remove = elias_encoder.encode_single_value(
            no_of_lzss_encodings
        )
        code = code[len(code_to_remove) :]

        lzss_encodings: List[EncodingType] = []
        for i in range(no_of_lzss_encodings):
            # Check first bit of LZSS encoding
            format_bit = int(code[0])
            code = code[1:]

            if format_bit == 0:
                # Decode Offset
                offset = elias_decoder.decode_single_value(code)
                code_to_remove = elias_encoder.encode_single_value(offset)
                code = code[len(code_to_remove) :]

                # Decode length
                length = elias_decoder.decode_single_value(code)
                code_to_remove = elias_encoder.encode_single_value(length)
                code = code[len(code_to_remove) :]
                lzss_encodings.append((0, offset, length))
            elif format_bit == 1:
                char, huffman_code = self.search_for_char(code)
                code = code[len(huffman_code) :]
                lzss_encodings.append((1, char))
            else:
                raise Exception

        decoder = lzss_decoder_class.LZSSDecoder(lzss_encodings)
        return decoder.decode()

    def search_for_char(self, code: str) -> Tuple[str, str]:
        values = self.huffman_coding.values()
        for value in values:
            match = True
            for i in range(len(value)):
                if code[i] != value[i]:
                    match = False
                    break
            if match is False:
                continue
            for key, val in self.huffman_coding.items():
                if val == value:
                    return key, val
        raise Exception
