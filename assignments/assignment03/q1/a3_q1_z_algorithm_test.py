# import z_algorithm
from . import z_algorithm


class TestZAlgorithm:
    def test_one(self):
        txt = "aabaabcaxaabaabcy"
        expected = [None, 1, 0, 3, 1, 0, 0, 1, 0, 7, 1, 0, 3, 1, 0, 0, 0]
        assert z_algorithm.z_array(txt, len(txt)) == expected

    def test_two(self):
        txt = "aabaab"
        expected = [None, 1, 0, 3, 1, 0]
        assert z_algorithm.z_array(txt, len(txt)) == expected

    def test_three(self):
        txt = "abcdabcd"
        expected = [None, 0, 0, 0, 4, 0, 0, 0]
        assert z_algorithm.z_array(txt, len(txt)) == expected

    def test_four(self):
        txt = "aabcaabxaaz"
        expected = [None, 1, 0, 0, 3, 1, 0, 0, 2, 1, 0]
        assert z_algorithm.z_array(txt, len(txt)) == expected
