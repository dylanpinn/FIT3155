"""Test Node implementation."""

# pylint: disable=R0201
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

    def test_children_no_child(self):
        """Returns null if no children."""
        node = Node(10)
        assert node.children() is None

    def test_children(self):
        """Returns iterable children."""
        parent = Node(10)
        children = [Node(1), Node(2), Node(3)]
        parent.child = children[0]
        for child in parent.children():
            assert child == children[0]
        parent.child.next = children[1]
        parent.child.next.next = children[2]
        for index, child in enumerate(parent.children()):
            assert child == children[index]
