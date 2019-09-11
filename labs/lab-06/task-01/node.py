"""Node to be used in double linked list in Fib Heap."""


class Node:
    """Fibonacci Heap Linked List Node."""

    def __init__(self, item):
        self.key = item
        self.mark = False
        self.degree = 0
        self.parent = None
        self.prev = None
        self.next = None
        self.child = None

    def children(self):
        """Iterate of the nodes children."""
        if self.child is None:
            return None
        return iter(self.child)

    def __iter__(self):
        current = self
        while current is not None:
            yield current
            current = current.next
