"""Fibonacci Heap."""

from node import Node
from circular_double_linked_list import CircularDoubleLinkedList

class FibonacciHeap:
    def __init__(self):
        # This will be a double-linked list
        self.root_nodes = CircularDoubleLinkedList()
        self.min = None
        self.size = 0

    def insert(self, item):
        """Insert item into heap."""
        node = Node(item)
        # list is empty
        if self.min is None:
            self.root_nodes.insert_beginning(node)
            self.min = node
        else:
            self.root_nodes.insert_before(self.min, node)
            if node.key < self.min.key:
                self.min = node
        self.size += 1
