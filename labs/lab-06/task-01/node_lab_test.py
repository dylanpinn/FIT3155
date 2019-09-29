"""Test Node implementation."""

import node as n


class TestLabNode:
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
        assert node.children() == []

    def test_children(self):
        """Returns iterable children."""
        parent = n.Node(10)
        items = [18, 52, 38]
        for item in items:
            parent.create_child(n.Node(item))
        arr = list(parent.children())
        assert len(arr) == 3
        for index, item in enumerate(items):
            found = False
            for node in arr:
                if item == node.key:
                    found = True
            assert found

    def test_create_child_no_children(self):
        """Test creating a child if non exists."""
        parent = n.Node(1)
        child = n.Node(2)
        parent.create_child(child)
        assert parent.child == child
        assert child.parent == parent

    def test_create_child_with_children(self):
        """Test creating a child if children exist."""
        parent = n.Node(1)
        existing_child = n.Node(3)
        parent.child = existing_child
        existing_child.parent = parent
        child_new = n.Node(2)
        parent.create_child(child_new)
        assert parent.child == existing_child
        assert parent.child.next == child_new
        assert child_new.parent == parent
        assert existing_child.parent == parent

    def test_remove_only_item_in_list(self):
        """Test removing an item from a list with only it in it."""
        node = n.Node(10)
        assert len(list(node)) == 1
        next_node = node.remove()
        assert next_node is None

    def test_remove_item_in_list(self):
        """Test removing item from a list."""
        node = n.Node(1)
        other_node = n.Node(2)
        node.insert(other_node)
        assert len(list(node)) == 2
        next_node = node.remove()
        assert len(list(next_node)) == 1
        assert next_node.key == other_node.key
