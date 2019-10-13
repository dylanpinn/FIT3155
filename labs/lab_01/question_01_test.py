import question_01


class TestGusfield:
    def test_one(self):
        txt = 'aabaabcaxaabaabcy'
        expected = [None, 1, 0, 3, 1, 0, 0, 1, 0, 7, 1, 0, 3, 1, 0, 0, 0]
        assert question_01.z_array(txt) == expected

    def test_two(self):
        txt = 'aabaab'
        expected = [None, 1, 0, 3, 1, 0]
        assert question_01.z_array(txt) == expected

    def test_three(self):
        txt = 'abcdabcd'
        expected = [None, 0, 0, 0, 4, 0, 0, 0]
        assert question_01.z_array(txt) == expected

    def test_four(self):
        txt = 'aabcaabxaaz'
        expected = [None, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]
        assert question_01.z_array(txt) == expected

    def test_match_no_find(self):
        pat = 'abcd'
        txt = 'abceabc'
        assert question_01.matches(pat, txt) is False

    def test_match_find(self):
        pat = 'abcd'
        txt = 'abcdabce'
        assert question_01.matches(pat, txt) is True
