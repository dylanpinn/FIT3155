"""
FIT3155 - Assignment 3

Semester 2 2019

Dylan Pinn 24160547
"""

import elias_encoder
import huffman_coding
import z_algorithm


class LZSSEncoder:
    def __init__(self, code: str, window_size: int, buffer_size: int):
        self.code = code
        self.window_size = window_size
        self.buffer_size = buffer_size
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

    def encode_data(self):
        data = ""
        encoding = self.lz77_encoding()
        print(encoding)

        return data

    @staticmethod
    def convert_to_8_bit_ascii(char: str) -> str:
        return "{0:0=8d}".format(int(bin(ord(char))[2:]))

    def lz77_encoding(self):
        i = 0
        encoding = []
        while i < len(self.code):
            #     prefix := longest prefix of input that begins in window
            prefix = self.find_prefix(i)

            #     if prefix exists then
            #         i := distance to start of prefix
            #         l := length of prefix
            #         c := char following prefix in input
            if prefix:
                val = prefix
            else:
                val = (0, 0, self.code[i])

            encoding.append(val)

            #     s := pop l+1 chars from front of input
            #     discard l+1 chars from front of window
            #     append s to back of window
            i += val[1] + 1
        return encoding

    def find_prefix(self, index: int):
        # Use z-algorithm to find longest prefix that matches.
        string = f"{self.__buffer(index)}"
        string += f"🎓{self.__dict(index)}{self.__buffer(index)}"
        print(string)
        index_to_stop = self.buffer_size + 1 + len(self.__dict(index))
        print(index_to_stop)
        z_array = z_algorithm.find_z_array(string, index_to_stop)
        print(z_array)
        dist_from_index = 1
        # TODO: Generate z_array starting at each character of dict.
        # No matches on prefix
        if z_array[self.buffer_size + 1] is None:
            i = 0
            l = 0
            c = self.code[index]  # first char of input
        else:
            # Find max value in remaining z_array
            remaining_list = z_array[self.buffer_size + 1 :]
            max_val = max(list(filter(None.__ne__, remaining_list)))
            i = dist_from_index  # distance to start of prefix
            l = max_val  # length of the prefix
            c = self.code[dist_from_index + 1]  # char following prefix in input
            print(max_val)
        return (i, l, c)

    def __buffer(self, index: int) -> str:
        """Return the current buffer from index."""
        return self.code[index : index + self.buffer_size]

    def __dict(self, index: int) -> str:
        """The current dictionary from index."""
        return self.code[max(0, index - self.window_size) : index]
