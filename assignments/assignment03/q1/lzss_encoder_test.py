import lzss_encoder


class TestLZSSEncoder:
    def test_example(self):
        code = "aacaacabcaba"
        window_size = 6
        look_buffer = 4
        result = lzss_encoder.encode_header(code)
        assert "011011000011101100010010000110001101001" == result
