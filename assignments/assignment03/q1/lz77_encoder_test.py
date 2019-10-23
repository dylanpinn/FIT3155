import pytest
import lz77_encoder


class TestLZSSEncoder:
    @pytest.mark.skip(reason="Waiting on find_prefix to be implemented")
    def test_example_data(self):
        code = "aacaacabcaba"
        window_size = 6
        look_buffer = 4
        encoder = lz77_encoder.LZSSEncoder(code, window_size, look_buffer)
        result = encoder.encode_data()
        assert "00011111111010011000100100001101111" == result

    def test_find_prefix(self):
        code = "aacaacabcabaaac"
        window_size = 6
        look_buffer = 4
        encoder = lz77_encoder.LZSSEncoder(code, window_size, look_buffer)
        result = encoder.find_prefix(0)
        assert (0, 0, "a") == result
        result = encoder.find_prefix(1)
        assert (1, 1, "c") == result
        result = encoder.find_prefix(3)
        assert (3, 4, "b") == result
        result = encoder.find_prefix(8)
        assert (3, 3, "a") == result
        result = encoder.find_prefix(12)
        assert (1, 2, "c") == result
