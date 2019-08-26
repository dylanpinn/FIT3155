import boyermoore


class TestBoyerMoore:
    def test_one(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        assert boyermoore.matches(txt, pat) is True
