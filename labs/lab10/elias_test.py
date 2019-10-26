import l_elias_decoder
import l_elias_encoder


class TestElias:
    def test_all(self):
        for i in range(1, 100000):
            code = l_elias_encoder.encode_single_value(i)
            decoded = l_elias_decoder.decode_single_value(code)
            assert i == decoded

    def test_joined(self):
        code = ""
        for i in range(1, 1000):
            code += l_elias_encoder.encode_single_value(i)
        for i in range(1, 1000):
            decoded = l_elias_decoder.decode_single_value(code)
            code = code[len(l_elias_encoder.encode_single_value(i)) :]
            assert i == decoded
