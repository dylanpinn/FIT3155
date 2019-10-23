"""
FIT3155 - Assignment 3

Semester 2 2019

Dylan Pinn 24160547


LZSS Encoder
"""

import z_algorithm


class LZSSEncoder:
    def __init__(self, code: str, window_size: int, buffer_size: int):
        self.code = code
        self.window_size = window_size
        self.buffer_size = buffer_size

    def encode(self):
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
        buffer = self.__buffer(index)
        dictionary = self.__dict(index)

        # Calculate longest prefix for each val in dictionary
        string = f"{buffer}🎓{dictionary}{buffer}"
        index_to_stop = len(buffer) + 1 + len(dictionary)
        z_array = z_algorithm.z_array(string, index_to_stop)
        # No matches on prefix
        if z_array[self.buffer_size + 1] is None:
            i = 0
            l = 0
            c = self.code[index]  # first char of input
        else:
            # Length of the current longest prefix.
            rem_list = z_array[self.buffer_size + 1 :]
            max_val = max(list(filter(None.__ne__, rem_list)))
            # distance to start of prefix
            i = index_to_stop - rem_list.index(max_val) - self.buffer_size - 1
            l = max_val  # length of the prefix
            # char following prefix in input
            c = self.code[index + max_val]

        return i, l, c

    def __buffer(self, index: int) -> str:
        """Return the current buffer from index."""
        return self.code[index : index + self.buffer_size]

    def __dict(self, index: int) -> str:
        """The current dictionary from index."""
        return self.code[max(0, index - self.window_size) : index]
