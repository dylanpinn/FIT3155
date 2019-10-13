import lzss_encoder
import huffman_coding


class TestLZSSEncoder:
    def test_example_header(self):
        code = "aacaacabcaba"
        huffman_values = huffman_coding.encoded_values(code)[0]
        result = lzss_encoder.encode_header(code, huffman_values)
        assert "011011000011101100010010000110001101001" == result

    def test_example_data(self):
        code = "aacaacabcaba"
        window_size = 6
        look_buffer = 4
        result = lzss_encoder.encode_data(code, window_size, look_buffer)
        assert "00011111111010011000100100001101111" == result
