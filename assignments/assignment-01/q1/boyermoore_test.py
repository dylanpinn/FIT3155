"""Tests for Assignment 1 - Q1."""
import pytest
import boyermoore


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

