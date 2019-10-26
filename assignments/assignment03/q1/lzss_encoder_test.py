from . import lzss_encoder


class TestLZSSEncoder:
    def test_header_from_assignment_sheet(self):
        expected = "011011000011101100010010000110001101001"
        encoder = lzss_encoder.Encoder("aacaacabcaba", 6, 4)
        result = encoder.encode_header()
        assert expected == result

    def test_data_from_assignment_sheet(self):
        expected = "00011111111010011000100100001101111"
        encoder = lzss_encoder.Encoder("aacaacabcaba", 6, 4)
        result = encoder.encode_data()
        assert expected == result
