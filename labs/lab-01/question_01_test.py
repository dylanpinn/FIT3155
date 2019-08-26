import question_01

class TestGusfield:
    def test_base_case_one(self):
        string = 'aab'
        expected = [None, 1, None]
        result, _, _ = question_01.base_case(string)
        assert result == expected  # nosec

    def test_base_case_two(self):
        string = 'abb'
        expected = [None, 0, None]
        result, _, _ = question_01.base_case(string)
        assert result == expected  # nosec

    def test_base_case_three(self):
        string = 'aaa'
        expected = [None, 2, None]
        result, _, _ = question_01.base_case(string)
        assert result == expected  # nosec

    def test_one(self):
        txt = 'aabaabcaxaabaabcy'
        expected = [None, 1, 0, 3, 1, 0, 0, 1, 0, 7, 1, 0, 3, 1, 0, 0, 0]
        assert question_01.gusfield(txt)[0] == expected  # nosec

    def test_two(self):
        txt = 'aabaab'
        expected = [None, 1, 0, 3, 1, 0]
        assert question_01.gusfield(txt)[0] == expected  # nosec

    def test_three(self):
        txt = 'abcdabcd'
        expected = [None, 0, 0, 0, 4, 0, 0, 0]
        assert question_01.gusfield(txt)[0] == expected  # nosec

    def test_four(self):
        txt = 'aabcaabxaaz'
        expected = [None, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]
        assert question_01.gusfield(txt)[0] == expected  # nosec

    def test_match_no_find(self):
        pat = 'abcd'
        txt = 'abceabc'
        assert question_01.find_match(pat, txt) is False  # nosec

    # def test_match_find(self):
    #     pat = 'abcd'
    #     txt = 'abcdabce'
    #     assert question_01.find_match(pat, txt) is True  # nosec
