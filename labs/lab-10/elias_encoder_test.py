import elias_encoder


class TestEliasEncoder:
    def test_from_lecture_slides(self):
        """Test using example from lecture slides."""
        expected = '00100011000110001'
        assert elias_encoder.encode(561) == expected
