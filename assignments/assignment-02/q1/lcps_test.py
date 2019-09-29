"""Tests for LCPS"""

import lcps


class TestLCPS:
    def test_generate_suffix_tree_simple_lecture(self):
        """Generate simple tree using lecture example."""
        text = 'abba'
        tree = lcps.SuffixTree(text)
        assert tree.n == 4
        assert tree.text == text
        root_edges = tree.root.filtered_edges
        assert len(root_edges) == 2
        assert root_edges[0].destination.index == 0
        assert root_edges[0].label == 'abba'
        assert root_edges[1].label == 'b'
        edges = root_edges[1].destination.filtered_edges
        assert len(edges) == 2
        assert edges[0].label == 'a'
        assert edges[0].destination.index == 2
        assert edges[1].label == 'ba'
        assert edges[1].destination.index == 1

    def test_suffix_tree_simple(self):
        """Test naively generating a suffix tree."""
        text = 'abc'
        tree = lcps.SuffixTree(text)
        assert len(tree.root.filtered_edges) == 3
        assert tree.root.filtered_edges[0].label == 'abc'
        assert tree.root.filtered_edges[1].label == 'bc'
        assert tree.root.filtered_edges[2].label == 'c'

    def test_generate_suffix_tree_simple_repetitions(self):
        """Test generating suffix tree with simple repetitions."""
        text = 'abcabxabcd'
        tree = lcps.SuffixTree(text)

    def test_generate_suffix_tree(self):
        """Test generating a suffix tree."""
        text = 'banana'
        tree = lcps.SuffixTree(text)
        edges = tree.root.filtered_edges
        assert len(edges) == 3
        assert edges[0].label == 'anana'
        assert edges[1].label == 'banana'
        assert edges[2].label == 'nana'

    def test_generate_suffix_tree_2(self):
        """Test generating a suffix tree."""
        text = 'mississippi'
        tree = lcps.SuffixTree(text)
        edges = tree.root.filtered_edges
        assert len(edges) == 4
        assert edges[0].label == 'i'
        assert len(edges[0].destination.filtered_edges) == 2
        assert edges[0].destination.filtered_edges[0].label == 'ppi'
        assert edges[0].destination.filtered_edges[0].destination.index == 7
        assert edges[0].destination.filtered_edges[1].label == 'ssi'
        assert len(edges[0].destination.filtered_edges[1].destination.filtered_edges) == 2
        assert edges[0].destination.filtered_edges[1].destination.filtered_edges[0].label == 'ppi'
        assert edges[0].destination.filtered_edges[1].destination.filtered_edges[0].destination.index == 4
        assert edges[0].destination.filtered_edges[1].destination.filtered_edges[1].label == 'ssippi'
        assert edges[0].destination.filtered_edges[1].destination.filtered_edges[1].destination.index == 1
        assert edges[1].label == 'mississippi'
        assert edges[1].destination.index == 0
        assert edges[2].label == 'p'
        assert len(edges[2].destination.filtered_edges) == 2
        assert edges[2].destination.filtered_edges[0].label == 'i'
        assert edges[2].destination.filtered_edges[0].destination.index == 9
        assert edges[2].destination.filtered_edges[1].label == 'pi'
        assert edges[2].destination.filtered_edges[1].destination.index == 8
        assert edges[3].label == 's'
        assert len(edges[3].destination.filtered_edges) == 2
        assert edges[3].destination.filtered_edges[0].label == 'i'
        assert len(edges[3].destination.filtered_edges[0].destination.filtered_edges) == 2
        assert edges[3].destination.filtered_edges[0].destination.filtered_edges[0].label == 'ppi'
        assert edges[3].destination.filtered_edges[0].destination.filtered_edges[0].destination.index == 6
        assert edges[3].destination.filtered_edges[0].destination.filtered_edges[1].label == 'ssippi'
        assert edges[3].destination.filtered_edges[0].destination.filtered_edges[1].destination.index == 3
        assert edges[3].destination.filtered_edges[1].label == 'si'
        assert len(edges[3].destination.filtered_edges[1].destination.filtered_edges) == 2
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[0].label == 'ppi'
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[0].destination.index == 5
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[1].label == 'ssippi'
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[1].destination.index == 2

    def test_generate_suffix_tree_3(self):
        """Test generating a suffix tree."""
        text = 'GATAGACA'
        tree = lcps.SuffixTree(text)
        edges = tree.root.filtered_edges
        assert len(edges) == 4

    def test_generate_suffix_tree_4(self):
        """Test generating a suffix tree."""
        text = 'aabbabaa'
        tree = lcps.SuffixTree(text)
        edges = tree.root.filtered_edges
        assert len(edges) == 2

    def test_suffix_tree(self):
        text = 'xyzxyaxyz$'
        tree = lcps.SuffixTree(text)
        assert tree.n == len(text)
        edges = tree.root.filtered_edges
        assert len(edges) == 5
        assert edges[0].label == '$'
        assert edges[0].start == 9
        assert int(edges[0].end) == 9
        assert edges[0].destination.index == 9
        assert edges[0].destination.link is None
        assert len(edges[0].destination.filtered_edges) == 0

        assert edges[1].label == 'axyz$'
        assert edges[1].start == 5
        assert int(edges[1].end) == 9
        assert edges[1].destination.index == 5
        assert edges[1].destination.link is None
        assert len(edges[1].destination.filtered_edges) == 0

        assert edges[2].label == 'xy'
        assert edges[2].start == 0
        assert int(edges[2].end) == 1
        assert edges[2].destination.index is None
        assert edges[2].destination.link.link == tree.root
        assert len(edges[2].destination.filtered_edges) == 2
        assert edges[2].destination.filtered_edges[0].label == 'axyz$'
        assert edges[2].destination.filtered_edges[0].start == 5
        assert int(edges[2].destination.filtered_edges[0].end) == 9
        assert edges[2].destination.filtered_edges[0].destination.index == 3
        assert edges[2].destination.filtered_edges[0].destination.link is None
        assert len(edges[2].destination.filtered_edges[0].destination.filtered_edges) == 0
        assert edges[2].destination.filtered_edges[1].label == 'z'
        assert edges[2].destination.filtered_edges[1].start == 2
        assert int(edges[2].destination.filtered_edges[1].end) == 2
        assert edges[2].destination.filtered_edges[1].destination.index is None
        assert edges[2].destination.filtered_edges[1].destination.link.link.link == tree.root
        assert len(edges[2].destination.filtered_edges[1].destination.filtered_edges) == 2
        assert edges[2].destination.filtered_edges[1].destination.filtered_edges[0].label == '$'
        assert edges[2].destination.filtered_edges[1].destination.filtered_edges[0].start == 9
        assert int(edges[2].destination.filtered_edges[1].destination.filtered_edges[0].end) == 9
        assert edges[2].destination.filtered_edges[1].destination.filtered_edges[0].destination.index == 6
        assert edges[2].destination.filtered_edges[1].destination.filtered_edges[0].destination.link is None
        assert len(edges[2].destination.filtered_edges[1].destination.filtered_edges[0].destination.filtered_edges) == 0
        assert edges[2].destination.filtered_edges[1].destination.filtered_edges[1].label == 'xyaxyz$'
        assert edges[2].destination.filtered_edges[1].destination.filtered_edges[1].start == 3
        assert int(edges[2].destination.filtered_edges[1].destination.filtered_edges[1].end) == 9
        assert edges[2].destination.filtered_edges[1].destination.filtered_edges[1].destination.index == 0
        assert edges[2].destination.filtered_edges[1].destination.filtered_edges[1].destination.link is None
        assert len(edges[2].destination.filtered_edges[1].destination.filtered_edges[1].destination.filtered_edges) == 0

        assert edges[3].label == 'y'
        assert edges[3].start == 1
        assert int(edges[3].end) == 1
        assert edges[3].destination.index is None
        assert edges[3].destination.link == tree.root
        assert len(edges[3].destination.filtered_edges) == 2
        assert edges[3].destination.filtered_edges[0].label == 'axyz$'
        assert edges[3].destination.filtered_edges[0].start == 5
        assert int(edges[3].destination.filtered_edges[0].end) == 9
        assert edges[3].destination.filtered_edges[0].destination.index == 4
        assert edges[3].destination.filtered_edges[0].destination.link is None
        assert len(edges[3].destination.filtered_edges[0].destination.filtered_edges) == 0
        assert edges[3].destination.filtered_edges[1].label == 'z'
        assert edges[3].destination.filtered_edges[1].start == 2
        assert int(edges[3].destination.filtered_edges[1].end) == 2
        assert edges[3].destination.filtered_edges[1].destination.index is None
        assert edges[3].destination.filtered_edges[1].destination.link.link == tree.root
        assert len(edges[3].destination.filtered_edges[1].destination.filtered_edges) == 2
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[0].label == '$'
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[0].start == 9
        assert int(edges[3].destination.filtered_edges[1].destination.filtered_edges[0].end) == 9
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[0].destination.index == 7
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[0].destination.link is None
        assert len(edges[3].destination.filtered_edges[1].destination.filtered_edges[0].destination.filtered_edges) == 0
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[1].label == 'xyaxyz$'
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[1].start == 3
        assert int(edges[3].destination.filtered_edges[1].destination.filtered_edges[1].end) == 9
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[1].destination.index == 1
        assert edges[3].destination.filtered_edges[1].destination.filtered_edges[1].destination.link is None
        assert len(edges[3].destination.filtered_edges[1].destination.filtered_edges[1].destination.filtered_edges) == 0

        assert edges[4].label == 'z'
        assert edges[4].start == 2
        assert int(edges[4].end) == 2
        assert edges[4].destination.index is None
        assert edges[4].destination.link == tree.root
        assert len(edges[4].destination.filtered_edges) == 2
        assert edges[4].destination.filtered_edges[0].label == '$'
        assert edges[4].destination.filtered_edges[0].start == 9
        assert int(edges[4].destination.filtered_edges[0].end) == 9
        assert edges[4].destination.filtered_edges[0].destination.index == 8
        assert edges[4].destination.filtered_edges[0].destination.link is None
        assert len(edges[4].destination.filtered_edges[0].destination.filtered_edges) == 0
        assert edges[4].destination.filtered_edges[1].label == 'xyaxyz$'
        assert edges[4].destination.filtered_edges[1].start == 3
        assert int(edges[4].destination.filtered_edges[1].end) == 9
        assert edges[4].destination.filtered_edges[1].destination.index == 2
        assert edges[4].destination.filtered_edges[1].destination.link is None
        assert len(edges[4].destination.filtered_edges[1].destination.filtered_edges) == 0

    def test_generate_suffix_tree_5(self):
        """Test generating a suffix tree."""
        text = 'mississi$'
        tree = lcps.SuffixTree(text)

    def test_find_lcps(self):
        """Test generating a suffix tree."""
        text = 'mississippi$'
        tree = lcps.SuffixTree(text)
        assert tree.find_lcps(8, 11) == 1
        assert tree.find_lcps(2, 5) == 4
        assert tree.find_lcps(1, 5) == 0
        assert tree.find_lcps(4, 7) == 2
