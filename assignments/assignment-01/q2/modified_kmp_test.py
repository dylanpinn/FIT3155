"""Tests for Assignment 1 - Question 2."""

import modified_kmp


class TestModifiedKMP:
    def test_match(self):
        pat = 'abc'
        txt = 'abcdabcdabcd'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)  # nosec

    def test_no_match(self):
        pat = 'abc'
        txt = 'abdaabdc'
        assert modified_kmp.match(pat, txt) == bool(pat in txt)  # nosec
