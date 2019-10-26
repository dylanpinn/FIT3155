from . import lzss_encoder


class TestLZSSEncoder:
    def test_from_assignment_sheet(self):
        expected = "011011000011101100010010000110001101001"
        result = lzss_encoder.encode_header("aacaacabcaba", 6, 4)
        assert expected == result
