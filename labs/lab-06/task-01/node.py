"""Node to be used in double linked list in Fib Heap."""

from typing import Union, Optional


class Node:
    """Fibonacci Heap Linked List Node."""
    key: Union[str, int]
    mark: bool
    degree: int
    parent: Optional['Node']
    prev: Optional['Node']
    next: Optional['Node']
    child: Optional['Node']

    def __init__(self, item: Union[str, int]):
        self.key = item
        self.mark = False
        self.degree = 0
        self.parent = self.child = None
        self.prev = self.next = self

    def children(self) -> iter('Node'):
        """Iterate of the nodes children."""
        if self.child is None:
            return []
        return list(self.child)

    def create_child(self, node: 'Node'):
        """Make a node a child of the current node."""
        node.parent = self
        if self.child is not None:
            self.child.insert(node)
        else:
            self.child = node
            self.degree = 1

    def insert(self, node: 'Node'):
        """Insert new node into double circular linked list."""
        node.next = self.next
        node.prev = self
        self.next.prev = node
        self.next = node

    def remove(self) -> Optional['Node']:
        """Remove a node from a double circular linked list return the next item in the list."""
        # if only item in list then remove and return None
        if self.prev == self and self.next == self:
            return None
        self.prev.next = self.next
        self.next.prev = self.prev
        next_node = self.next
        return next_node

    def merge(self, node: 'Node'):
        """Merge two lists together."""
        self.next.prev = node.prev
        node.prev.next = self.next
        self.next = node
        node.prev = self

    def __iter__(self):
        """Iterate once over nodes in double linked list."""
        first = current = self
        while current != first.prev:
            yield current
            current = current.next
        if current == first.prev:
            yield current
