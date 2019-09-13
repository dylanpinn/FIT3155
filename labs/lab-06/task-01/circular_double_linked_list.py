"""Circular Double Linked List."""

from node import Node


class CircularDoubleLinkedList:
    """Circular Double Linked List."""

    def __init__(self):
        self.size = 0
        self.last = None

    def insert_before(self, node, new_node):
        """Insert a new node before an existing node.
        :param node: Existing Node
        :type node: Node
        :param new_node: New Node to insert.
        :type node: Node
        """
        self.insert_after(node.prev, new_node)

    def insert_after(self, node, new_node):
        """Insert a new node after an existing node.
        :param node: Existing Node
        :type node: Node
        :param new_node: New Node to insert.
        :type new_node: Node
        """
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node
        self.size += 1

    def insert_end(self, node):
        """Insert a node at the end of the list.
        :param node: New Node to insert.
        :type node: Node
        """
        if self.last is None:
            node.prev = node
            node.next = node
            self.size += 1
        else:
            self.insert_after(self.last, node)
        self.last = node

    def remove(self, node):
        """Remove node from list.
        :param node: Node to remove from list.
        :type node: Node
        """
        if node.next == node:
            self.last = None
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            if node == self.last:
                self.last = node.prev
        del node
        self.size -= 1
