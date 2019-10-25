from . import lzss_encoder


class TestLZSSEncoder:
    def test_encode_string(self):
        code = "aacaacabcabaaac"
        window_size = 6
        look_buffer = 4
        encoder = lzss_encoder.LZSSEncoder(code, window_size, look_buffer)
        result = encoder.encode()
        expected = [
            (0, 0, "a"),
            (1, 1, "c"),
            (3, 4, "b"),
            (3, 3, "a"),
            (1, 2, "c"),
        ]
        assert expected == result

    def test_encode_single(self):
        code = "aacaacabcabaaac"
        window_size = 6
        look_buffer = 4
        encoder = lzss_encoder.LZSSEncoder(code, window_size, look_buffer)
        result = encoder.encode_single(0)
        assert (0, 0, "a") == result
        result = encoder.encode_single(1)
        assert (1, 1, "c") == result
        result = encoder.encode_single(3)
        assert (3, 4, "b") == result
        result = encoder.encode_single(8)
        assert (3, 3, "a") == result
        result = encoder.encode_single(12)
        assert (1, 2, "c") == result
