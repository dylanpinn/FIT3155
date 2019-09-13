"""Fibonacci Heap."""

import math
from typing import List, Union, Optional

from circular_double_linked_list import CircularDoubleLinkedList
from node import Node


class FibonacciHeap:
    """Fibonacci Heap using double linked list."""
    root_nodes: CircularDoubleLinkedList
    min: Optional[Node]
    size: int

    def __init__(self):
        # This will be a double-linked list
        self.root_nodes = CircularDoubleLinkedList()
        self.min = None
        self.size = 0

    def insert(self, item: Union[str, int]):
        """Insert item into heap."""
        node = Node(item)
        # list is empty
        if self.min is None:
            self.root_nodes.insert_end(node)
            self.min = node
        else:
            self.root_nodes.insert_before(self.min, node)
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
                    self.root_nodes.insert_before(current, child)
                    child.parent = None
            self.root_nodes.remove(min_node)
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
        for w in self.min:
            x: Node = w
            d = x.degree
            while aux_array[d] is not None:
                y: Node = aux_array[d]  # another node with same degree as x
                if x.key > y.key:
                    aux_array[d] = x
                self.link(y, x)
                aux_array[d] = None
                d += 1

            aux_array[d] = x
        self.min = None
        for i in range(aux_size):
            if aux_array[i] is not None:
                if self.min is None:
                    self.root_nodes = CircularDoubleLinkedList()
                    self.root_nodes.insert_end(aux_array[i])
                    self.min = aux_array[i]
                else:
                    self.root_nodes.insert_end(aux_array[i])
                    if aux_array[i].key < self.min.key:
                        self.min = aux_array[i]

    def link(self, child: Node, parent: Node):
        """Link 2 nodes making one a child of another.
        :param child: Node which will become a child of the parent.
        :type child: Node
        :param parent: Node which will become parent of the child.
        :type parent: Node
        """
        self.root_nodes.remove(child)
        parent.child.create_child(child)
        child.mark = False

    def __sizeof_aux_array(self):
        """Return size of auxiliary array used for consolidate."""
        return math.floor(math.log2(self.size))

    # TODO: merge
    # TODO: decrease-key
    # TODO: delete
