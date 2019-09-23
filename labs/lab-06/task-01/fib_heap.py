"""Fibonacci Heap."""

import math
from typing import List, Union, Optional

from node import Node


class FibonacciHeap:
    """Fibonacci Heap using double linked list."""
    root_nodes: Optional[Node]
    min: Optional[Node]
    size: int

    def __init__(self):
        self.root_nodes = None
        self.min = None
        self.size = 0

    def insert(self, item: Union[str, int]):
        """Insert item into heap."""
        node = Node(item)
        # list is empty
        if self.min is None:
            self.root_nodes = node
            self.min = node
        else:
            self.root_nodes.insert(node)
            if node.key < self.min.key:
                self.min = node
        self.size += 1

    def extract_min(self) -> Union[str, int]:
        """Extract min value from heap."""
        min_node = self.min
        if min_node is not None:
            current = min_node.next
            if min_node.child:
                for child in min_node.children():
                    # Insert into root nodes before current
                    current.prev.insert(child)
                    child.parent = None
            # if min_node is root_node pointer then change to next after removing
            if min_node == self.root_nodes:
                self.root_nodes = min_node.remove()
            else:
                min_node.remove()
            if min_node == min_node.next:
                self.min = None
            else:
                self.min = current
                self.consolidate()
            self.size -= 1

        return min_node.key

    def consolidate(self):
        """Consolidate Heap."""
        aux_size = self.__sizeof_aux_array()
        aux_array: List[Optional[Node]] = [None] * aux_size
        nodes = list(self.root_nodes)
        nodes = nodes[nodes.index(self.min):] + nodes[:nodes.index(self.min)]
        for w in nodes:
            x: Node = w
            d = x.degree
            while aux_array[d] is not None:
                y: Node = aux_array[d]  # another node with same degree as x
                if x.key > y.key:
                    tmp = y
                    y = x
                    x = tmp
                self.link(y, x)
                aux_array[d] = None
                d += 1

            aux_array[d] = x
        self.min = None
        self.root_nodes = None
        for i in range(aux_size):
            if aux_array[i] is not None:
                if self.min is None:
                    self.root_nodes = aux_array[i]
                    self.min = aux_array[i]
                else:
                    self.root_nodes.insert(aux_array[i])
                    if aux_array[i].key < self.min.key:
                        self.min = aux_array[i]

    def link(self, child: Node, parent: Node):
        """Link 2 nodes making one a child of another.
        :param child: Node which will become a child of the parent.
        :type child: Node
        :param parent: Node which will become parent of the child.
        :type parent: Node
        """
        # Remove child from root_nodes
        if self.root_nodes == child:
            self.root_nodes = child.remove()
        else:
            child.remove()
        child.next = child.prev = child
        parent.degree += 1
        parent.create_child(child)
        child.mark = False

    def __sizeof_aux_array(self):
        """Return size of auxiliary array used for consolidate."""
        return math.ceil(math.log2(self.size))

    # TODO: merge
    # TODO: decrease-key
    # TODO: delete
