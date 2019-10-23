import pytest

from . import encoder


class TestEncoder:
    # From assignment sheet.
    @pytest.mark.skip(reason="Need to implement.")
    def test_example_data(self):
        code = "aacaacabcaba"
        window_size = 6
        look_buffer = 4
        enc = encoder.Encoder(code, window_size, look_buffer)
        result = enc.encode()
        assert "00011111111010011000100100001101111" == result

    def test_example_header(self):
        code = "aacaacabcaba"
        enc = encoder.Encoder(code)
        result = enc.encode_header()
        assert "011011000011101100010010000110001101001" == result
