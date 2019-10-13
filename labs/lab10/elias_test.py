import elias_decoder
import elias_encoder


class TestElias:
    def test_all(self):
        for i in range(1, 100000):
            code = elias_encoder.encode_single_value(i)
            decoded = elias_decoder.decode_single_value(code)
            assert i == decoded

    def test_joined(self):
        code = ""
        for i in range(1, 1000):
            code += elias_encoder.encode_single_value(i)
        for i in range(1, 1000):
            decoded = elias_decoder.decode_single_value(code)
            code = code[len(elias_encoder.encode_single_value(i)) :]
            assert i == decoded
