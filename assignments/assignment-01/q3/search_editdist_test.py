import pytest

from q3 import search_editdist


class TestSearchEditDist:
    @pytest.mark.skip(reason="not completed")
    def test_search_edit_dist_1(self):
        txt = 'abdyabxdcyabcdz'
        pat = 'abcd'
        expected = [(1, 1), (5, 1), (11, 0)]
        assert search_editdist.search(pat, txt) == expected

    def test_find_match(self):
        txt = '990099abcd9999'
        pat = 'abcd'
        expected = [(7, 0)]
        assert search_editdist.search(pat, txt) == expected

    def test_sub_start(self):
        txt = 'bcd0000000'
        pat = 'ccd'
        expected = [(0, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_sub_middle(self):
        txt = '0000000abdddya4568'
        pat = 'abcddy'
        expected = [(7, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_sub_end(self):
        txt = '000000abcdef'
        pat = 'cdeh'
        expected = [(8, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_insert_start(self):
        txt = 'bcd1100000000'
        pat = 'abcd'
        expected = [(0, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_insert_middle(self):
        txt = '999999abdya00000'
        pat = 'abcd'
        expected = [(6, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_insert_end(self):
        txt = '0000000abcdef'
        pat = 'defg'
        expected = [(10, 1)]
        assert search_editdist.search(pat, txt, 0) == expected
