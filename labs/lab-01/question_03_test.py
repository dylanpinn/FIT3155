import question_03


class TestRandomStringGen:
    def test_length(self):
        """It returns string of correct length."""
        result = question_03.generate(5, 0.5)
        assert len(result) == 5
        result = question_03.generate(7, 0.5)
        assert len(result) == 7
