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
        decoder = lzss_decoder_class.LZSSDecoder(code)
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
        decoder = lzss_decoder_class.LZSSDecoder(code)
        result = decoder.decode()
        expected = "aacaacabcaba"
        assert expected == result
