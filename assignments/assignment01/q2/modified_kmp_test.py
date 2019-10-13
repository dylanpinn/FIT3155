"""Tests for Assignment 1 - Question 2."""
import random
import re
import string

import pytest

import modified_kmp


def random_string(string_length=10):
    """Generates a random string of a fixed length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(string_length))


class TestModifiedKMP:
    def test_suffix_prefix(self):
        pat = 'bbccaebbcabd'
        expected = [0, 1, 0, 0, 0, 0, 0, 1, 3, 0, 1, 0]
        assert modified_kmp.compute_suffix_prefix(pat) == expected

    def test_match(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)

    def test_no_match(self):
        pat = 'abc'
        txt = 'abdaabdc'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)

    def test_kmp_match(self):
        """Test matches on first iteration."""
        pat = 'abc'
        txt = 'abcdabc'
        assert modified_kmp.match(pat, txt) is True

    def test_match_2(self):
        """Test matches on further iteration."""
        pat = 'abc'
        txt = 'abcdabcd'
        assert modified_kmp.match(pat, txt) is True

    def test_no_match_6(self):
        """Test no matches."""
        pat = 'abc'
        txt = 'abdabdabe'
        assert modified_kmp.match(pat, txt) is False

    def test_incorrect_len(self):
        """Test no match when pattern > text."""
        pat = 'abcd'
        txt = 'abc'
        assert modified_kmp.match(pat, txt) is False

    def test_no_match_2(self):
        """Test no match when pattern > text."""
        pat = 'Ap'
        txt = 'poFfTzfHQAOD9Duwe9eB3gRaJIGIgyW35DWJjplV'
        assert modified_kmp.match(pat, txt) is False

    def test_no_match_3(self):
        """Test no match when pattern > text."""
        pat = '6FjKojoBhRk8YbMH9fau0fHk9S38S5LcJ2LSzOApSw9ScEOlN4p0bKbbLlmurKYG0epr5O3RrU2avmQA1pPK02'  # noqa: E501
        txt = '02mTAg8avVRF01uKrsuuLJzKU36WzL6VUJiHvBDQxfA7PoN4vy9JR7oEg3x76yeRsEOOoDRNmwfXgEXIlmtjJrEwSp7ptRwFquP8u0'  # noqa: E501
        assert modified_kmp.match(pat, txt) == bool(pat in txt)

    def test_no_match_4(self):
        """Test no match when pattern > text."""
        pat = 'l'
        txt = 'lFx0OyuczjmH'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)

    @pytest.mark.skip("TODO: Fix")
    def test_match_kmp(self):
        pat = 'abcaby'
        txt = 'abxabcabcaby'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)

    def test_match_all(self):
        for i in range(2, 1000):
            pat = random_string(random.randint(1, i))
            txt = random_string(i)
            expected = bool(pat in txt)
            assert modified_kmp.match(pat, txt) == expected

    def test_kmp_algorithm(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        expected = [1, 5, 9]
        assert modified_kmp.kmp(pat, txt) == expected

    @pytest.mark.skip("TODO: Fix")
    def test_kmp_algorithm_other(self):
        pat = 'abcdabcy'
        txt = 'abcxabcdabcdabcy'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_match_1(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_match_13(self):
        pat = '33'
        txt = 'abc'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_match_0(self):
        """Test matches on first iteration."""
        pat = 'abc'
        txt = 'abcdabc'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_match_2(self):
        """Test matches on further iteration."""
        pat = 'abc'
        txt = 'abcdabcd'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_no_match(self):
        """Test no matches."""
        pat = 'abc'
        txt = 'abdabdabe'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_incorrect_len(self):
        """Test no match when pattern > text."""
        pat = 'abcd'
        txt = 'abc'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_no_match_2(self):
        """Test no match when pattern > text."""
        pat = 'Ap'
        txt = 'poFfTzfHQAOD9Duwe9eB3gRaJIGIgyW35DWJjplV'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_no_match_3(self):
        """Test no match when pattern > text."""
        pat = '6FjKojoBhRk8YbMH9fau0fHk9S38S5LcJ2LSzOApSw9ScEOlN4p0bKbbLlmurKYG0epr5O3RrU2avmQA1pPK02'  # noqa: E501
        txt = '02mTAg8avVRF01uKrsuuLJzKU36WzL6VUJiHvBDQxfA7PoN4vy9JR7oEg3x76yeRsEOOoDRNmwfXgEXIlmtjJrEwSp7ptRwFquP8u0'  # noqa: E501
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    def test_kmp_no_match_4(self):
        """Test no match when pattern > text."""
        pat = 'l'
        txt = 'lFx0OyuczjmH'
        expected = [m.start() for m in re.finditer(pat, txt)]
        assert modified_kmp.kmp(pat, txt, 0) == expected

    @pytest.mark.skip("TODO: Fix")
    def test_all_kmp(self):
        for i in range(2, 1000):
            pat = random_string(random.randint(1, i))
            txt = random_string(i)
            expected = [m.start() for m in re.finditer(pat, txt)]
            assert modified_kmp.kmp(pat, txt, 0) == expected
