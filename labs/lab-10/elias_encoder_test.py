import elias_encoder


class TestEliasEncoder:
    def test_from_lecture_slides(self):
        """Test using example from lecture slides."""
        expected = '00100011000110001'
        assert elias_encoder.encode_single_value(561) == expected

    def test_multiple_values(self):
        expected = '0010001100011000100100011000110001'
        assert elias_encoder.encode([561, 561]) == (2, expected)

    def test_multiple_values_2(self):
        expected = '001000110001100010010001100011000100000010000'
        assert elias_encoder.encode([561, 561, 16]) == (3, expected)
