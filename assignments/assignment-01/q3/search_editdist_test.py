import pytest
from q3 import search_editdist


class TestSearchEditDist:
    def test_search_edit_dist_1(self):
        txt = 'abdyabxdcyabcdz'
        pat = 'abcd'
        expected = [(1, 1), (5, 1), (11, 0)]
        assert search_editdist.search(pat, txt) == expected

    def test_find_match(self):
        txt = 'abdyabxdcyabcdz'
        pat = 'abcd'
        expected = [(11, 0)]
        assert search_editdist.search(pat, txt) == expected

    def test_insert_start(self):
        txt = 'bcd'
        pat = 'abcd'
        expected = [(0, 1)]
        assert search_editdist.search(pat, txt, 0) == expected
