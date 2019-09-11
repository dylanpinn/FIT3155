"""Node to be used in doubley linked list in Fib Heap."""


class Node:
    def __init__(self, item):
        self.key = item
        self.mark = False
        self.degree = 0
        self.parent = None
        self.prev = None
        self.next = None
        self.child = None
