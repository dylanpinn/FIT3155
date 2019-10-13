import huffman_coding
import elias_encoder


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
        result = ""
        res = huffman_coding.unique_chars(code)
        result += elias_encoder.encode_single_value(len(res))
        for val in res:
            result += elias_encoder.encode_single_value(res[val])
            result += str(ord(val))
        result += elias_encoder.encode_single_value(len(code))
        result += huffman_coding.encode(code)

        decoded_value = huffman_coding.decode(result)
        print(result)
