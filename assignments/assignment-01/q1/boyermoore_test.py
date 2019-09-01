"""Tests for Assignment 1 - Q1."""
import string
import random
import pytest
import boyermoore


def random_string(string_length=10):
    """Generates a random string of a fixed length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(string_length))

class TestBoyerMoore:
    """Test Class."""
    @pytest.mark.skip(reason="TEMP SKIP")
    def test_one(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        assert boyermoore.matches(txt, pat) is True  # nosec

    @pytest.mark.skip(reason="TEMP SKIP")
    def test_no_match(self):
        pat = 'abc'
        txt = 'abdaabdc'
        assert boyermoore.matches(txt, pat) is False  # nosec

    def test_badchar(self):
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

    def test_naive_match(self):
        """Test matches on first iteration."""
        pat = 'abc'
        txt = 'abcdabc'
        assert boyermoore.naive_algorithm(pat, txt) is True  # nosec

    def test_naive_match_2(self):
        """Test matches on further iteration."""
        pat = 'abc'
        txt = 'abcdabcd'
        assert boyermoore.naive_algorithm(pat, txt) is True  # nosec

    def test_naive_no_match(self):
        """Test no matches."""
        pat = 'abc'
        txt = 'abdabdabe'
        assert boyermoore.naive_algorithm(pat, txt) is False  # nosec


    def test_naive_incorrect_len(self):
        """Test no match when pattern > text."""
        pat = 'abcd'
        txt = 'abc'
        assert boyermoore.naive_algorithm(pat, txt) is False  # nosec

    def test_naive_no_match_2(self):
        """Test no match when pattern > text."""
        pat = 'Ap'
        txt = 'poFfTzfHQAOD9Duwe9eB3gRaJIGIgyW35DWJjplV'
        assert boyermoore.naive_algorithm(pat, txt) is False  # nosec

    @pytest.mark.skip(reason="TEMP SKIP")
    def test_all_naive(self):
        for i in range(2, 1000):
            pat = random_string(random.randint(1, i))
            txt = random_string(i)
            expected = bool(pat in txt)
            assert boyermoore.naive_algorithm(pat, txt) == expected  # nosec
