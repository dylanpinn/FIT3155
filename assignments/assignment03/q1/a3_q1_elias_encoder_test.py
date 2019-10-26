import elias_encoder


class TestEliasEncoder:
    def test_from_lecture_slides(self):
        """Test using example from lecture slides."""
        expected = "00100011000110001"
        assert elias_encoder.encode_single_value(561) == expected

    def test_multiple_values(self):
        expected = "0010001100011000100100011000110001"
        assert elias_encoder.encode([561, 561]) == (2, expected)

    def test_multiple_values_2(self):
        expected = "001000110001100010010001100011000100000010000"
        assert elias_encoder.encode([561, 561, 16]) == (3, expected)

    def test_more_values(self):
        expected = "1"
        assert elias_encoder.encode_single_value(1) == expected
        expected = "010"
        assert elias_encoder.encode_single_value(2) == expected
        expected = "011"
        assert elias_encoder.encode_single_value(3) == expected
        expected = "000100"
        assert elias_encoder.encode_single_value(4) == expected
        expected = "000101"
        assert elias_encoder.encode_single_value(5) == expected
        expected = "000110"
        assert elias_encoder.encode_single_value(6) == expected
        expected = "000111"
        assert elias_encoder.encode_single_value(7) == expected
        expected = "0011000"
        assert elias_encoder.encode_single_value(8) == expected
        expected = "0011001"
        assert elias_encoder.encode_single_value(9) == expected
        expected = "0011010"
        assert elias_encoder.encode_single_value(10) == expected
        expected = "0011111"
        assert elias_encoder.encode_single_value(15) == expected
        expected = "00000010000"
        assert elias_encoder.encode_single_value(16) == expected
