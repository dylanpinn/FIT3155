from q3 import search_editdist


class TestSearchEditDist:
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
        pat = 'acd'
        expected = [(0, 1), (1, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_sub_middle(self):
        txt = '00000000abdddya456800'
        pat = 'abcddy'
        expected = [(8, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_sub_end(self):
        txt = '000000abcdef'
        pat = 'cdeh'
        expected = [(8, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_sub_end_2(self):
        txt = '00abefx'
        pat = 'efh'
        expected = [(4, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_insert_start(self):
        txt = 'bcd1100000000000'
        pat = 'abcd'
        expected = [(0, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_insert_middle(self):
        txt = '999999abdya00000'
        pat = 'abcd'
        expected = [(6, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_insert_middle_2(self):
        txt = '99abdya00'
        pat = 'abcd'
        expected = [(2, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_insert_end(self):
        txt = '0000000abcdef'
        pat = 'defg'
        expected = [(10, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_insert_end_2(self):
        txt = '0000cdef'
        pat = 'defg'
        expected = [(5, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_del_middle(self):
        txt = '999999abXcdef00000'
        pat = 'abcdef'
        expected = [(6, 1)]
        assert search_editdist.search(pat, txt, 0) == expected

    def test_del_middle_2(self):
        txt = '9999abcdefXgh00000'
        pat = 'abcdefgh'
        expected = [(4, 1)]
        assert search_editdist.search(pat, txt, 0) == expected
