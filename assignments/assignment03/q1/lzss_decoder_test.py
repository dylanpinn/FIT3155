from . import lzss_decoder


class TestLZSSEncoder:
    def test_from_assignment_sheet(self):
        expected = "aacaacabcaba"
        encoder = lzss_decoder.Decoder(
            "01101100001110110001001000011000110100100011111111010011000100100001101111"
        )
        result = encoder.decode()
        assert expected == result
