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
        if self.child is not None:
            self.child.insert(node)
        else:
            node.prev = node.next = node
            self.child = node
            self.degree = 1

    def insert(self, node: 'Node'):
        """Insert new node into double circular linked list."""
        node.next = self.next
        node.prev = self
        self.next.prev = self.next = node

    def __iter__(self):
        """Iterate over nodes in double linked list."""
        first = current = self
        while current != first.prev:
            yield current
            current = current.next
        if current == first.prev:
            yield current
