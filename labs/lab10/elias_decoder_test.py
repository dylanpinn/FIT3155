import l_elias_decoder


class TestEliasDecoder:
    def test_from_lecture_slides(self):
        """Test using example from lecture slides."""
        expected = 561
        assert (
            l_elias_decoder.decode_single_value("00100011000110001")
            == expected
        )

    def test_multiple_values(self):
        expected = [561, 561]
        assert (
            l_elias_decoder.decode(["00100011000110001", "00100011000110001"])
            == expected
        )

    def test_multiple_values_2(self):
        expected = [561, 561, 16]
        assert (
            l_elias_decoder.decode(
                ["00100011000110001", "00100011000110001", "00000010000"]
            )
            == expected
        )
