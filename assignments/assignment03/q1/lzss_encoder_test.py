from . import lzss_encoder


class TestLZSSEncoder:
    def test_from_assignment_sheet(self):
        expected = "011011000011101100010010000110001101001"
        encoder = lzss_encoder.Encoder("aacaacabcaba", 6, 40)
        result = encoder.encode_header()
        assert expected == result
