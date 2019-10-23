from . import encoder


class TestEncoder:
    def test_example_header(self):
        code = "aacaacabcaba"
        enc = encoder.Encoder(code)
        result = enc.encode_header()
        assert "011011000011101100010010000110001101001" == result
