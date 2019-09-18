"""Test Circular Double Linked List implementation."""

import circular_double_linked_list
import node


# pylint: disable=R0201
class TestCircularDoubleLinkedList:
    """Test CircularDoubleLinkedList."""

    def test_initial_size(self):
        """Lists have initial size of 0."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        assert linked_list.size == 0

    def test_initial_last(self):
        """Lists have no initial last node."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        assert linked_list.last is None

    def test_insert_new_list(self):
        """Test inserting into an empty list."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        n = node.Node(10)
        linked_list.insert_end(n)
        assert linked_list.last is n
        assert linked_list.size == 1
        assert n.prev is n
        assert n.next is n

    def test_insert_end(self):
        """Test inserting into a list at end."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        node1 = node.Node(10)
        linked_list.insert_end(node1)
        node2 = node.Node(5)
        linked_list.insert_end(node2)
        assert linked_list.last is node2
        assert linked_list.last.next is node1
        assert linked_list.size == 2

    def test_insert_before(self):
        """Test inserting before an existing list."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        node1 = node.Node(10)
        linked_list.insert_end(node1)
        node2 = node.Node(5)
        linked_list.insert_end(node2)
        node3 = node.Node(9)
        linked_list.insert_before(node1, node3)
        assert linked_list.last is node2
        assert linked_list.last.next is node3
        assert linked_list.last.next.next is node1
        assert linked_list.last.next.next.next is node2
        assert linked_list.size == 3

    def test_remove_item_first(self):
        """Test removing first item in list."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        node1 = node.Node(10)
        linked_list.insert_end(node1)
        node2 = node.Node(5)
        linked_list.insert_end(node2)
        node3 = node.Node(9)
        linked_list.insert_end(node3)
        assert linked_list.last is node3
        assert linked_list.last.next is node1
        assert linked_list.size == 3
        linked_list.remove(node1)
        assert linked_list.last is node3
        assert linked_list.last.next is node2
        assert linked_list.size == 2

    def test_remove_item_last(self):
        """Test removing last item in list."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        node1 = node.Node(1)
        linked_list.insert_end(node1)
        node2 = node.Node(2)
        linked_list.insert_end(node2)
        node3 = node.Node(3)
        linked_list.insert_end(node3)
        assert linked_list.last is node3
        assert linked_list.size == 3
        linked_list.remove(node3)
        assert linked_list.last is node2
        assert linked_list.size == 2

    def test_remove_item(self):
        """Test removing a item in middle of the list."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        node1 = node.Node(10)
        linked_list.insert_end(node1)
        node2 = node.Node(9)
        linked_list.insert_end(node2)
        node3 = node.Node(8)
        linked_list.insert_end(node3)
        assert linked_list.last.next is node1
        assert linked_list.last is node3
        assert linked_list.size == 3
        linked_list.remove(node2)
        assert linked_list.last is node3
        assert linked_list.last.next is node1
        assert linked_list.last.next.next is node3
        assert linked_list.size == 2

    def test_remove_list_single_item(self):
        """Test removing item from a list with one item."""
        linked_list = circular_double_linked_list.CircularDoubleLinkedList()
        n = node.Node(100)
        linked_list.insert_end(n)
        assert linked_list.last is n
        assert linked_list.size == 1
        linked_list.remove(n)
        assert linked_list.last is None
        assert linked_list.size == 0
