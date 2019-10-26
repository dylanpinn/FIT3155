import random
import string

import huffman_coding


def random_string(string_length=10):
    """Generates a random string of a fixed length."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(string_length))


class TestHuffmanCoding:
    def test_number_of_unique_chars(self):
        code = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        result = huffman_coding.unique_chars(code)
        assert len(result) == 6

    def test_freq_of_chars(self):
        code = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        result = huffman_coding.unique_chars(code)
        assert result["C"] == 2
        assert result["B"] == 6
        assert result["E"] == 7
        assert result["_"] == 10
        assert result["D"] == 10
        assert result["A"] == 11

    def test_huffman(self):
        code = "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        result = huffman_coding.encode_header(code)
        result += huffman_coding.encode(code)
        decoded_value = huffman_coding.decode(result)
        assert (
            decoded_value == "A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        )

    def test_more(self):
        codes = ["ao"]
        for code in codes:
            result = huffman_coding.encode_header(code)
            result += huffman_coding.encode(code)
            decoded_value = huffman_coding.decode(result)
            assert decoded_value == code

    def test_random(self):
        for i in range(2, 1000):
            code = random_string(random.randint(1, i))
            result = huffman_coding.encode_header(code)
            result += huffman_coding.encode(code)
            decoded_value = huffman_coding.decode(result)
            assert decoded_value == code
