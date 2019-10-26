import random
import string

import lzss_decoder
import lzss_encoder


def random_string(string_length=10):
    """Generates a random string of a fixed length."""
    chars = string.printable
    return "".join(random.choice(chars) for _ in range(string_length))


def random_number(end_value):
    """Generate a random number between 2 and end_value"""
    return random.randint(1, end_value)


class TestEncoder:
    def test_random(self):
        for i in range(1, 1000):
            print("new iteration")
            code = random_string(random.randint(1, i))
            buffer_size = random_number(len(code))
            window_size = random_number(len(code))
            print(code)
            print(window_size)
            print(buffer_size)
            encoder = lzss_encoder.Encoder(code, window_size, buffer_size)
            encoded_value = encoder.encode()
            print(encoded_value)

            decoder = lzss_decoder.Decoder(encoded_value)
            decoded_value = decoder.decode()

            assert decoded_value == code
