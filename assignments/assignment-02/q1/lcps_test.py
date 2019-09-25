"""Tests for LCPS"""

import lcps


class TestLCPS:
    def test_generate_suffixes(self):
        """Test generating suffixes for a given text."""
        text = 'banana$'
        expected = ['banana$', 'anana$', 'nana$', 'ana$', 'na$', 'a$', '$']
        assert lcps.generate_suffixes(text) == expected

    def test_generate_suffix_tree_simple_lecture(self):
        """Generate simple tree using lecture example."""
        text = 'abba'
        tree = lcps.generate_suffix_tree(text)
        assert tree.n == 4
        assert tree.text == text
        root_edges = list(filter(None, tree.root.edges))
        assert len(root_edges) == 2
        assert root_edges[0].destination.suffix_index == 0
        assert root_edges[1].start == 1
        assert root_edges[1].end == 1

    # def test_generate_suffix_tree_simple(self):
    #     """Test naively generating a suffix tree."""
    #     text = 'abc'
    #     tree = lcps.generate_suffix_tree(text)
    #     assert tree.current_end.end == 2
    #     assert len(tree.root.edges) == 3
    #     for i in range(len(tree.root.edges)):
    #         assert tree.root.edges[i].start == i
    #         assert tree.root.edges[i].end.end == 2
    #
    # def test_generate_suffix_tree_simple_repetitions(self):
    #     """Test generating suffix tree with simple repetitions."""
    #     text = 'abcabxabcd'
    #     tree = lcps.generate_suffix_tree(text)

    # def test_naive_generate_suffix_tree(self):
    #     """Test naively generating a suffix tree."""
    #     text = 'abcab$'
    #     lcps.naive_generate_suffix_tree(text)
