"""Test Fibonacci Heap implementation."""

import circular_double_linked_list as cir
import fib_heap
import node


def heap_from_slides():
    """Create Fib Heap from lecture slides."""
    root_nodes = cir.CircularDoubleLinkedList()
    root_nodes.insert_end(node.Node(23))
    root_nodes.insert_end(node.Node(7))
    parent = node.Node(3)
    min_node = parent
    sub_node = node.Node(18)
    sub_node.list = cir.CircularDoubleLinkedList()
    sub_node.list.insert_end(sub_node)
    sub_node.list.insert_end(node.Node(52))
    sub_sub_node = node.Node(38)
    sub_sub_node.degree = 1
    sub_sub_node.create_child(node.Node(41))
    sub_node.list.insert_end(sub_sub_node)
    sub_node.create_child(node.Node(39))
    parent.create_child(sub_node)
    sub_node.degree = 1
    parent.degree = 2
    root_nodes.insert_end(parent)
    parent = node.Node(17)
    parent.create_child(node.Node(30))
    parent.degree = 1
    root_nodes.insert_end(parent)
    parent = node.Node(24)
    sub_node = node.Node(26)
    sub_node.list = cir.CircularDoubleLinkedList()
    sub_node.list.insert_end(sub_node)
    sub_node.list.insert_end(node.Node(46))
    sub_node.create_child(node.Node(35))
    parent.create_child(sub_node)
    sub_node.degree = 1
    parent.degree = 2
    root_nodes.insert_end(parent)
    heap = fib_heap.FibonacciHeap()
    heap.root_nodes = root_nodes
    heap.size = 14
    heap.min = min_node
    return heap


class TestFibonacciHeap:
    def test_initial_min(self):
        """Initial min should be nil."""
        heap = fib_heap.FibonacciHeap()
        assert heap.min is None

    def test_initial_size(self):
        """Initial size should be 0."""
        heap = fib_heap.FibonacciHeap()
        assert heap.size == 0

    def test_insert_empty(self):
        """Test inserting into an empty Heap."""
        heap = fib_heap.FibonacciHeap()
        heap.insert(1)
        assert heap.min.key == 1
        assert heap.size == 1

    def test_insert(self):
        """Test inserting ino a non-empty Heap."""
        heap = fib_heap.FibonacciHeap()
        heap.insert(10)
        heap.insert(5)
        assert heap.min.key == 5
        assert heap.root_nodes.size == 2
        assert heap.size == 2

    def test_insert_from_slides(self):
        """Test inserting into a heap using example from lecture slides."""
        heap = heap_from_slides()
        assert heap.root_nodes.size == 5
        heap.insert(21)
        assert heap.root_nodes.size == 6
        assert heap.size == 15

    def test_extract_min(self):
        """Test extracting min value from heap."""
        heap = fib_heap.FibonacciHeap()
        heap.insert(10)
        heap.insert(5)
        heap.insert(3)
        heap.insert(100)
        assert heap.min.key == 3
        assert heap.size == 4
        min_node = heap.extract_min()
        assert min_node == 3
        assert heap.size == 3
        assert heap.min.key == 5

    def test_extract_min_from_slides(self):
        """Test extract min using lecture slides example."""
        heap = heap_from_slides()
        heap.insert(21)
        assert heap.root_nodes.size == 6
        assert heap.size == 15
        min_node = heap.extract_min()
        assert min_node == 3
        assert heap.root_nodes.size == 3
        assert heap.size == 14
        assert heap.min.degree == 3
        assert heap.min.child.list.size == 3
