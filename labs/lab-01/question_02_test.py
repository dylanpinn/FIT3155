import question_02


class TestNaive:
    def test_one(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        assert question_02.naive(pat, txt) == bool(pat in txt)

    def test_two(self):
        pat = 'abc'
        txt = 'abdaabdc'
        assert question_02.naive(pat, txt) == bool(pat in txt)

    def test_three(self):
        pat = 'abc'
        txt = 'abcdabc'
        assert question_02.naive(pat, txt) == bool(pat in txt)

    def test_four(self):
        pat = 'abc'
        txt = 'abcdabcd'
        assert question_02.naive(pat, txt) == bool(pat in txt)

    def test_match_no_find(self):
        """Test no matches."""
        pat = 'abc'
        txt = 'abdabdabe'
        assert question_02.naive(pat, txt) == bool(pat in txt)

    def test_incorrect_len(self):
        """Test no match when pattern > text."""
        pat = 'abcd'
        txt = 'abc'
        assert question_02.naive(pat, txt) == bool(pat in txt)
