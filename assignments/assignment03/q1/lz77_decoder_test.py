from . import lz77_decoder


class TestLZ77Decoder:
    def test_decode_string(self):
        code = [
            (0, 0, "a"),
            (1, 1, "c"),
            (3, 4, "b"),
            (3, 3, "a"),
            (1, 2, "c"),
        ]
        window_size = 6
        look_buffer = 4
        decoder = lz77_decoder.LZ77Decoder(code, window_size, look_buffer)
        result = decoder.decode()
        expected = "aacaacabcabaaac"
        assert expected == result
