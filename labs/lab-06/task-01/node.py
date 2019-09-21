"""Node to be used in double linked list in Fib Heap."""

from typing import Union, Optional

import circular_double_linked_list as cir


class Node:
    """Fibonacci Heap Linked List Node."""
    key: Union[str, int]
    mark: bool
    degree: int
    parent: Optional['Node']
    prev: Optional['Node']
    next: Optional['Node']
    child: Optional['Node']
    list: Optional[cir.CircularDoubleLinkedList]

    def __init__(self, item: Union[str, int]):
        self.key = item
        self.mark = False
        self.degree = 0
        self.parent = None
        self.prev = None
        self.next = None
        self.child = None
        self.list = None

    def children(self) -> iter('Node'):
        """Iterate of the nodes children."""
        if self.child is None:
            return None
        return list(self.child.list)

    def create_child(self, node: 'Node'):
        """Make a node a child of the current node."""
        if self.child is not None:
            self.child.list.insert_end(node)
        else:
            self.child = node
            self.degree = 1
            if node.list is None:
                node.list = cir.CircularDoubleLinkedList()
                node.list.insert_end(self.child)
