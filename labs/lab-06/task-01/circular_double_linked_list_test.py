"""Test Circular Double Linked List implementation."""

from circular_double_linked_list import CircularDoubleLinkedList
from node import Node


# pylint: disable=R0201
class TestCircularDoubleLinkedList:
    """Test CircularDoubleLinkedList."""

    def test_initial_size(self):
        """Lists have initial size of 0."""
        linked_list = CircularDoubleLinkedList()
        assert linked_list.size == 0

    def test_initial_first(self):
        """Lists have no initial first node."""
        linked_list = CircularDoubleLinkedList()
        assert linked_list.first is None

    def test_initial_last(self):
        """Lists have no initial last node."""
        linked_list = CircularDoubleLinkedList()
        assert linked_list.last is None

    def test_insert_new_list(self):
        """Test inserting into an empty list."""
        linked_list = CircularDoubleLinkedList()
        node = Node(10)
        linked_list.insert_beginning(node)
        assert linked_list.first is node
        assert linked_list.last is node
        assert linked_list.size == 1
        assert node.prev is None
        assert node.next is None

    def test_insert_beginning(self):
        """Test inserting into a list at beginning."""
        linked_list = CircularDoubleLinkedList()
        node1 = Node(10)
        linked_list.insert_beginning(node1)
        node2 = Node(5)
        linked_list.insert_beginning(node2)
        assert linked_list.first is node2
        assert linked_list.last is node1
        assert linked_list.size == 2

    def test_insert_before(self):
        """Test inserting before an existing list."""
        linked_list = CircularDoubleLinkedList()
        node1 = Node(10)
        linked_list.insert_beginning(node1)
        node2 = Node(5)
        linked_list.insert_beginning(node2)
        node3 = Node(9)
        linked_list.insert_before(node1, node3)
        assert linked_list.first is node2
        assert linked_list.last is node1
        assert linked_list.size == 3

    def test_remove_item_first(self):
        """Test removing first item in list."""
        linked_list = CircularDoubleLinkedList()
        node1 = Node(10)
        linked_list.insert_beginning(node1)
        node2 = Node(5)
        linked_list.insert_beginning(node2)
        node3 = Node(9)
        linked_list.insert_beginning(node3)
        assert linked_list.first is node3
        assert linked_list.size == 3
        linked_list.remove(node3)
        assert linked_list.first is node2
        assert linked_list.size == 2


    def test_remove_item_last(self):
        """Test removing last item in list."""
        linked_list = CircularDoubleLinkedList()
        node1 = Node(10)
        linked_list.insert_beginning(node1)
        node2 = Node(5)
        linked_list.insert_beginning(node2)
        node3 = Node(9)
        linked_list.insert_beginning(node3)
        assert linked_list.last is node1
        assert linked_list.size == 3
        linked_list.remove(node1)
        assert linked_list.last is node2
        assert linked_list.size == 2

    def test_remove_item(self):
        """Test removing a item in middle of the list."""
        linked_list = CircularDoubleLinkedList()
        node1 = Node(10)
        linked_list.insert_beginning(node1)
        node2 = Node(5)
        linked_list.insert_beginning(node2)
        node3 = Node(9)
        linked_list.insert_beginning(node3)
        assert linked_list.first is node3
        assert linked_list.last is node1
        assert linked_list.size == 3
        linked_list.remove(node2)
        assert linked_list.first is node3
        assert linked_list.last is node1
        assert linked_list.size == 2
