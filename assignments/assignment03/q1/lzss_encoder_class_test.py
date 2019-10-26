from . import lzss_encoder_class


class TestLZSSEncoderClass:
    def test_encode_string(self):
        code = "aacaacabcabaaac"
        window_size = 6
        look_buffer = 4
        encoder = lzss_encoder_class.LZSSEncoder(
            code, window_size, look_buffer
        )
        result = encoder.encode()
        expected = [
            (1, "a"),
            (1, "a"),
            (1, "c"),
            (0, 3, 4),
            (1, "b"),
            (0, 3, 3),
            (1, "a"),
            (1, "a"),
            (1, "a"),
            (1, "c"),
        ]
        assert expected == result

    def test_encode_string_2(self):
        code = "aacaacabcaba"
        window_size = 6
        look_buffer = 4
        encoder = lzss_encoder_class.LZSSEncoder(
            code, window_size, look_buffer
        )
        result = encoder.encode()
        expected = [
            (1, "a"),
            (1, "a"),
            (1, "c"),
            (0, 3, 4),
            (1, "b"),
            (0, 3, 3),
            (1, "a"),
        ]
        assert expected == result
