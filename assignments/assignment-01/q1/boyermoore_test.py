"""Tests for Assignment 1 - Q1."""
import string
import random
import re
import boyermoore


def random_string(string_length=10):
    """Generates a random string of a fixed length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(string_length))  # nosec


class TestBoyerMoore:
    """Test Class."""
    def test_match(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        assert boyermoore.match(pat, txt) == bool(pat in txt)  # nosec

    def test_no_match(self):
        pat = 'abc'
        txt = 'abdaabdc'
        assert boyermoore.match(pat, txt) == bool(pat in txt)  # nosec

    def test_boyer_match(self):
        """Test matches on first iteration."""
        pat = 'abc'
        txt = 'abcdabc'
        assert boyermoore.match(pat, txt) is True  # nosec

    def test_match_2(self):
        """Test matches on further iteration."""
        pat = 'abc'
        txt = 'abcdabcd'
        assert boyermoore.match(pat, txt) is True  # nosec

    def test_no_match_6(self):
        """Test no matches."""
        pat = 'abc'
        txt = 'abdabdabe'
        assert boyermoore.match(pat, txt) is False  # nosec

    def test_incorrect_len(self):
        """Test no match when pattern > text."""
        pat = 'abcd'
        txt = 'abc'
        assert boyermoore.match(pat, txt) is False  # nosec

    def test_no_match_2(self):
        """Test no match when pattern > text."""
        pat = 'Ap'
        txt = 'poFfTzfHQAOD9Duwe9eB3gRaJIGIgyW35DWJjplV'
        assert boyermoore.match(pat, txt) is False  # nosec

    def test_no_match_3(self):
        """Test no match when pattern > text."""
        pat = '6FjKojoBhRk8YbMH9fau0fHk9S38S5LcJ2LSzOApSw9ScEOlN4p0bKbbLlmurKYG0epr5O3RrU2avmQA1pPK02'
        txt = '02mTAg8avVRF01uKrsuuLJzKU36WzL6VUJiHvBDQxfA7PoN4vy9JR7oEg3x76yeRsEOOoDRNmwfXgEXIlmtjJrEwSp7ptRwFquP8u0'
        assert boyermoore.match(pat, txt) == bool(pat in txt)  # nosec

    def test_no_match_4(self):
        """Test no match when pattern > text."""
        pat = 'l'
        txt = 'lFx0OyuczjmH'
        assert boyermoore.match(pat, txt) == bool(pat in txt)  # nosec

    def test_naive(self):
        for i in range(2, 1000):
            pat = random_string(random.randint(1, i))  # nosec
            txt = random_string(i)
            expected = bool(pat in txt)
            assert boyermoore.match(pat, txt) == expected  # nosec

    def test_bad_char(self):
        expected = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, 0, 1, 2, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
                    -1]
        pat = 'ABC'
        assert boyermoore.calculate_bad_char_shift(pat) == expected  # nosec

    # TODO: Test good suffix
    # TODO: Test matched prefix

    def test_boyer_algorithm(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        expected = [1, 5, 9]
        assert boyermoore.boyer_moore(pat, txt) == expected  # nosec

    def test_boyer_match_1(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec

    def test_boyer_match_0(self):
        """Test matches on first iteration."""
        pat = 'abc'
        txt = 'abcdabc'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec

    def test_boyer_match_2(self):
        """Test matches on further iteration."""
        pat = 'abc'
        txt = 'abcdabcd'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec

    def test_boyer_no_match(self):
        """Test no matches."""
        pat = 'abc'
        txt = 'abdabdabe'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec

    def test_boyer_incorrect_len(self):
        """Test no match when pattern > text."""
        pat = 'abcd'
        txt = 'abc'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec

    def test_boyer_no_match_2(self):
        """Test no match when pattern > text."""
        pat = 'Ap'
        txt = 'poFfTzfHQAOD9Duwe9eB3gRaJIGIgyW35DWJjplV'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec

    def test_boyer_no_match_3(self):
        """Test no match when pattern > text."""
        pat = '6FjKojoBhRk8YbMH9fau0fHk9S38S5LcJ2LSzOApSw9ScEOlN4p0bKbbLlmurKYG0epr5O3RrU2avmQA1pPK02'
        txt = '02mTAg8avVRF01uKrsuuLJzKU36WzL6VUJiHvBDQxfA7PoN4vy9JR7oEg3x76yeRsEOOoDRNmwfXgEXIlmtjJrEwSp7ptRwFquP8u0'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec

    def test_boyer_no_match_4(self):
        """Test no match when pattern > text."""
        pat = 'l'
        txt = 'lFx0OyuczjmH'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec

    def test_all_boyer(self):
        for i in range(2, 1000):
            pat = random_string(random.randint(1, i))  # nosec
            txt = random_string(i)
            expected = [m.start() for m in re.finditer(pat, txt)]
            assert boyermoore.boyer_moore(pat, txt, 0) == expected  # nosec
