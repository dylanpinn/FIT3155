"""Test Node implementation."""

import circular_double_linked_list as cir

import node as n


class TestNode:
    """Test Node implementation."""

    def test_initial_mark(self):
        """A node should not be marked initially."""
        node = n.Node(10)
        assert node.mark is False

    def test_initial_degree(self):
        """A new node should have degree 0."""
        node = n.Node(10)
        assert node.degree == 0

    def test_construct_node(self):
        """A newly constructed node has its key set to the passed in item."""
        node = n.Node(5)
        assert node.key == 5

    def test_initial_parent(self):
        """A new node should have no parent."""
        node = n.Node(10)
        assert node.parent is None

    def test_initial_child(self):
        """A new node should have no child."""
        node = n.Node(10)
        assert node.child is None

    def test_children_no_child(self):
        """Returns null if no children."""
        node = n.Node(10)
        assert node.children() is None

    def test_children(self):
        """Returns iterable children."""
        parent = n.Node(10)
        children = [n.Node(1), n.Node(2), n.Node(3)]
        parent.child = children[0]
        for child in parent.children():
            assert child == children[0]
        parent.child.next = children[1]
        parent.child.next.next = children[2]
        for index, child in enumerate(parent.children()):
            assert child == children[index]

    def test_create_child_no_children(self):
        """Test creating a child if non exists."""
        parent = n.Node(1)
        child = n.Node(2)
        parent.create_child(child)
        assert parent.child == child
        assert parent.child.list is not None

    def test_create_child_with_children(self):
        """Test creating a child if children exist."""
        parent = n.Node(1)
        existing_child = n.Node(3)
        parent.child = existing_child
        parent.child.list = cir.CircularDoubleLinkedList()
        child_new = n.Node(2)
        parent.create_child(child_new)
        assert parent.child == existing_child
        assert parent.child.list.last == child_new
