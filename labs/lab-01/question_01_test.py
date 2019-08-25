import question_01

class TestGusfield:
    def test_one(self):
        pat = 'aab'
        txt = 'aabaabcaxaabaabcy'
        expected = [None, 1, 0, 3, 1, 0, 0, 1, 0, 7, 1, 0, 3, 1, 0, 0, 0]
        assert question_01.gusfield(pat, txt) == expected  # nosec
