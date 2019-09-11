"""Test Node implementation."""

from node import Node


class TestNode:
    """Test Node implementation."""
    def test_initial_mark(self):
        """A node should not be marked initially."""
        node = Node(10)
        assert node.mark is False

    def test_initial_degree(self):
        """A new node should have degree 0."""
        node = Node(1)
        assert node.degree == 0

    def test_construct_node(self):
        """A newly constructed node has its key set to the passed in item."""
        node = Node(5)
        assert node.key == 5

    def test_initial_parent(self):
        """A new node should have no parent."""
        node = Node(20)
        assert node.parent is None

    def test_initial_child(self):
        """A new node should have no child."""
        node = Node(0)
        assert node.child is None
