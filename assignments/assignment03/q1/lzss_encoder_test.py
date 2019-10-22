import pytest
import lzss_encoder
import huffman_coding


class TestLZSSEncoder:
    def test_example_header(self):
        code = "aacaacabcaba"
        window_size = 6
        look_buffer = 4
        encoder = lzss_encoder.LZSSEncoder(code, window_size, look_buffer)
        result = encoder.encode_header()
        assert "011011000011101100010010000110001101001" == result

    @pytest.mark.skip(reason="Waiting on find_prefix to be implemented")
    def test_example_data(self):
        code = "aacaacabcaba"
        window_size = 6
        look_buffer = 4
        encoder = lzss_encoder.LZSSEncoder(code, window_size, look_buffer)
        result = encoder.encode_data()
        assert "00011111111010011000100100001101111" == result

    def test_find_prefix(self):
        code = "aacaacabcabaaac"
        window_size = 6
        look_buffer = 4
        encoder = lzss_encoder.LZSSEncoder(code, window_size, look_buffer)
        result = encoder.find_prefix(0)
        assert (0, 0, "a") == result
