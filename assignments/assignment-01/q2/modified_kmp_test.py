"""Tests for Assignment 1 - Question 2."""
import string
import random
import re
from q2 import modified_kmp


def random_string(string_length=10):
    """Generates a random string of a fixed length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(string_length))  # nosec


class TestModifiedKMP:
    def test_match(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)  # nosec

    def test_no_match(self):
        pat = 'abc'
        txt = 'abdaabdc'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)  # nosec

    def test_boyer_match(self):
        """Test matches on first iteration."""
        pat = 'abc'
        txt = 'abcdabc'
        assert modified_kmp.match(pat, txt) is True  # nosec

    def test_match_2(self):
        """Test matches on further iteration."""
        pat = 'abc'
        txt = 'abcdabcd'
        assert modified_kmp.match(pat, txt) is True  # nosec

    def test_no_match_6(self):
        """Test no matches."""
        pat = 'abc'
        txt = 'abdabdabe'
        assert modified_kmp.match(pat, txt) is False  # nosec

    def test_incorrect_len(self):
        """Test no match when pattern > text."""
        pat = 'abcd'
        txt = 'abc'
        assert modified_kmp.match(pat, txt) is False  # nosec

    def test_no_match_2(self):
        """Test no match when pattern > text."""
        pat = 'Ap'
        txt = 'poFfTzfHQAOD9Duwe9eB3gRaJIGIgyW35DWJjplV'
        assert modified_kmp.match(pat, txt) is False  # nosec

    def test_no_match_3(self):
        """Test no match when pattern > text."""
        pat = '6FjKojoBhRk8YbMH9fau0fHk9S38S5LcJ2LSzOApSw9ScEOlN4p0bKbbLlmurKYG0epr5O3RrU2avmQA1pPK02'
        txt = '02mTAg8avVRF01uKrsuuLJzKU36WzL6VUJiHvBDQxfA7PoN4vy9JR7oEg3x76yeRsEOOoDRNmwfXgEXIlmtjJrEwSp7ptRwFquP8u0'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)  # nosec

    def test_no_match_4(self):
        """Test no match when pattern > text."""
        pat = 'l'
        txt = 'lFx0OyuczjmH'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)  # nosec

    def test_naive(self):
        for i in range(2, 1000):
            pat = random_string(random.randint(1, i))  # nosec
            txt = random_string(i)
            expected = bool(pat in txt)
            assert modified_kmp.match(pat, txt) == expected  # nosec
