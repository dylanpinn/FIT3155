"""Tests for LCPS"""

import lcps


# noinspection PyProtectedMember
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
        root_edges = tree.root._filtered_edges
        assert len(root_edges) == 2
        assert root_edges[0].destination.index == 0
        assert root_edges[0].label == 'abba'
        assert root_edges[1].label == 'b'
        edges = root_edges[1].destination._filtered_edges
        assert len(edges) == 2
        assert edges[0].label == 'a'
        assert edges[0].destination.index == 2
        assert edges[1].label == 'ba'
        assert edges[1].destination.index == 1

    def test_suffix_tree_simple(self):
        """Test naively generating a suffix tree."""
        text = 'abc'
        tree = lcps.generate_suffix_tree(text)
        assert len(tree.root._filtered_edges) == 3
        assert tree.root._filtered_edges[0].label == 'abc'
        assert tree.root._filtered_edges[1].label == 'bc'
        assert tree.root._filtered_edges[2].label == 'c'

    def test_generate_suffix_tree_simple_repetitions(self):
        """Test generating suffix tree with simple repetitions."""
        text = 'abcabxabcd'
        tree = lcps.generate_suffix_tree(text)

    def test_generate_suffix_tree(self):
        """Test generating a suffix tree."""
        text = 'banana'
        tree = lcps.generate_suffix_tree(text)
        edges = tree.root._filtered_edges
        assert len(edges) == 3
        assert edges[0].label == 'anana'
        assert edges[1].label == 'banana'
        assert edges[2].label == 'nana'

    def test_generate_suffix_tree_2(self):
        """Test generating a suffix tree."""
        text = 'mississippi'
        tree = lcps.generate_suffix_tree(text)
        edges = tree.root._filtered_edges
        assert len(edges) == 4
        assert edges[0].label == 'i'
        assert len(edges[0].destination._filtered_edges) == 2
        assert edges[0].destination._filtered_edges[0].label == 'ppi'
        assert edges[0].destination._filtered_edges[0].destination.index == 7
        assert edges[0].destination._filtered_edges[1].label == 'ssi'
        assert len(edges[0].destination._filtered_edges[1].destination._filtered_edges) == 2
        assert edges[0].destination._filtered_edges[1].destination._filtered_edges[0].label == 'ppi'
        assert edges[0].destination._filtered_edges[1].destination._filtered_edges[0].destination.index == 4
        assert edges[0].destination._filtered_edges[1].destination._filtered_edges[1].label == 'ssippi'
        assert edges[0].destination._filtered_edges[1].destination._filtered_edges[1].destination.index == 1
        assert edges[1].label == 'mississippi'
        assert edges[1].destination.index == 0
        assert edges[2].label == 'p'
        assert len(edges[2].destination._filtered_edges) == 2
        assert edges[2].destination._filtered_edges[0].label == 'i'
        assert edges[2].destination._filtered_edges[0].destination.index == 9
        assert edges[2].destination._filtered_edges[1].label == 'pi'
        assert edges[2].destination._filtered_edges[1].destination.index == 8
        assert edges[3].label == 's'
        assert len(edges[3].destination._filtered_edges) == 2
        assert edges[3].destination._filtered_edges[0].label == 'i'
        assert len(edges[3].destination._filtered_edges[0].destination._filtered_edges) == 2
        assert edges[3].destination._filtered_edges[0].destination._filtered_edges[0].label == 'ppi'
        assert edges[3].destination._filtered_edges[0].destination._filtered_edges[0].destination.index == 6
        assert edges[3].destination._filtered_edges[0].destination._filtered_edges[1].label == 'ssippi'
        assert edges[3].destination._filtered_edges[0].destination._filtered_edges[1].destination.index == 3
        assert edges[3].destination._filtered_edges[1].label == 'si'
        assert len(edges[3].destination._filtered_edges[1].destination._filtered_edges) == 2
        assert edges[3].destination._filtered_edges[1].destination._filtered_edges[0].label == 'ppi'
        assert edges[3].destination._filtered_edges[1].destination._filtered_edges[0].destination.index == 5
        assert edges[3].destination._filtered_edges[1].destination._filtered_edges[1].label == 'ssippi'
        assert edges[3].destination._filtered_edges[1].destination._filtered_edges[1].destination.index == 2

    def test_generate_suffix_tree_3(self):
        """Test generating a suffix tree."""
        text = 'GATAGACA'
        tree = lcps.generate_suffix_tree(text)
        edges = tree.root._filtered_edges
        assert len(edges) == 4

    def test_generate_suffix_tree_4(self):
        """Test generating a suffix tree."""
        text = 'aabbabaa'
        tree = lcps.generate_suffix_tree(text)
        edges = tree.root._filtered_edges
        assert len(edges) == 2
