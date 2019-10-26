from . import lzss_decoder_class


class TestLZSSDecoder:
    def test_decode_string(self):
        code = [
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
        window_size = 6
        look_buffer = 4
        decoder = lzss_decoder_class.LZSSDecoder(
            code, window_size, look_buffer
        )
        result = decoder.decode()
        expected = "aacaacabcabaaac"
        assert expected == result

    def test_decode_string_2(self):
        code = [
            (1, "a"),
            (1, "a"),
            (1, "c"),
            (0, 3, 4),
            (1, "b"),
            (0, 3, 3),
            (1, "a"),
        ]
        window_size = 6
        look_buffer = 4
        decoder = lzss_decoder_class.LZSSDecoder(
            code, window_size, look_buffer
        )
        result = decoder.decode()
        expected = "aacaacabcaba"
        assert expected == result
