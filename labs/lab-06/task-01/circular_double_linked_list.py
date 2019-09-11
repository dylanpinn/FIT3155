"""Circular Double Linked List."""


class CircularDoubleLinkedList:
    """Circular Double Linked List."""

    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def insert_beginning(self, node):
        """Insert a node at the 'start' of the list."""
        if self.first is None:
            self.first = node
            self.last = node
            node.prev = None
            node.next = None
            self.size += 1
        else:
            self.insert_before(self.first, node)

    def insert_before(self, node, new_node):
        """Insert a new node before an existing node."""
        new_node.next = node
        if node.prev is None:
            new_node.prev = None
            self.first = new_node
        else:
            new_node.prev = node.prev
            node.prev.next = new_node
        node.prev = new_node
        self.size += 1

    def remove(self, node):
        """Remove node from list."""
        if node.prev is None:
            self.first = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1
