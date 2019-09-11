"""Fibonacci Heap."""

from circular_double_linked_list import CircularDoubleLinkedList
from node import Node


class FibonacciHeap:
    """Fibonacci Heap using double linked list."""

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

    def extract_min(self):
        """Extract min value from heap."""
        min_node = self.min
        if min_node is not None:
            current = min_node.next
            if min_node.child:
                for child in min_node.children():
                    self.root_nodes.insert_before(current, child)
                    child.parent = None
            self.root_nodes.remove(min_node)
            if min_node == min_node.next:
                self.min = None
            else:
                self.min = current
                self.consolidate()
            self.size -= 1

        return min_node

    def consolidate(self):
        """Consolidate Heap."""
        # TODO: Complete
        pass

    # TODO: merge
    # TODO: decrease-key
    # TODO: delete
