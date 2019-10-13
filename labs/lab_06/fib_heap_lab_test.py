"""Test Fibonacci Heap implementation."""

import fib_heap
import node


def heap_from_slides():
    """Create Fib Heap from lecture slides."""
    root_nodes = parent = node.Node(24)
    sub_node = node.Node(26)
    sub_node.mark = True
    sub_node.parent = parent
    sub_node.insert(sub_node)
    n = node.Node(46)
    n.parent = parent
    sub_node.insert(n)
    sub_node.create_child(node.Node(35))
    parent.create_child(sub_node)
    sub_node.degree = 1
    parent.degree = 2
    parent = node.Node(17)
    parent.create_child(node.Node(30))
    parent.degree = 1
    root_nodes.insert(parent)
    parent = node.Node(3)
    min_node = parent
    sub_node = node.Node(18)
    sub_node.mark = True
    sub_node.insert(sub_node)
    sub_sub_node = node.Node(38)
    sub_sub_node.degree = 1
    sub_sub_node.create_child(node.Node(41))
    sub_sub_node.parent = sub_node
    sub_node.insert(sub_sub_node)
    n = node.Node(52)
    n.parent = sub_node
    sub_node.insert(n)
    n = node.Node(39)
    n.mark = True
    sub_node.create_child(n)
    parent.create_child(sub_node)
    sub_node.degree = 1
    parent.degree = 2
    root_nodes.insert(parent)
    root_nodes.insert(node.Node(7))
    root_nodes.insert(node.Node(23))

    heap = fib_heap.FibonacciHeap()
    heap.root_nodes = root_nodes
    heap.size = 14
    heap.min = min_node
    return heap


class TestFibonacciHeapLab:
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
        assert len(list(heap.root_nodes)) == 2
        assert heap.size == 2

    def test_insert_from_slides(self):
        """Test inserting into a heap using example from lecture slides."""
        heap = heap_from_slides()
        assert len(list(heap.root_nodes)) == 5
        heap.insert(21)
        assert len(list(heap.root_nodes)) == 6
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
        assert min_node.key == 3
        assert heap.size == 3
        assert heap.min.key == 5

    def test_extract_min_from_slides(self):
        """Test extract min using lecture slides example."""
        heap = heap_from_slides()
        heap.min.prev.insert(node.Node(21))
        heap.size += 1
        assert len(list(heap.root_nodes)) == 6
        assert heap.size == 15
        min_node = heap.extract_min()
        assert min_node.key == 3
        root_nodes = list(heap.root_nodes)
        assert len(root_nodes) == 3
        for item in [7, 18, 38]:
            found = False
            for n in root_nodes:
                if item == n.key:
                    found = True
            assert found
        assert heap.size == 14
        assert heap.min.degree == 3

        min_children = list(heap.min.child)
        assert len(min_children) == 3
        for item in [24, 17, 23]:
            found = False
            for n in min_children:
                if item == n.key:
                    found = True
            assert found

    def test_merge_heaps(self):
        """Test merging empty and non-empty heap"""
        heap1 = fib_heap.FibonacciHeap()
        heap1.insert(1)
        heap1.insert(2)
        heap1.insert(3)
        heap2 = fib_heap.FibonacciHeap()
        new_heap = heap2.merge(heap1)
        assert new_heap.size == 3
        assert len(list(new_heap.root_nodes)) == 3

    def test_merge_heaps_2(self):
        """Test merging empty and non-empty heap"""
        heap1 = fib_heap.FibonacciHeap()
        heap1.insert(4)
        heap1.insert(6)
        heap1.insert(7)
        heap2 = fib_heap.FibonacciHeap()
        new_heap = heap1.merge(heap2)
        assert new_heap.size == 3
        assert len(list(new_heap.root_nodes)) == 3

    def test_merge_heaps_3(self):
        """Test merging empty and non-empty heap"""
        heap1 = fib_heap.FibonacciHeap()
        heap1.insert(1)
        heap1.insert(2)
        heap1.insert(3)
        heap2 = fib_heap.FibonacciHeap()
        heap1.insert(4)
        heap1.insert(6)
        heap1.insert(7)
        new_heap = heap1.merge(heap2)
        assert new_heap.size == 6
        assert len(list(new_heap.root_nodes)) == 6

    def test_decrease_key(self):
        """Test decrease key using lecture slide example."""
        heap = heap_from_slides()
        heap.min.prev.insert(node.Node(21))
        heap.size += 1
        heap.extract_min()
        n = heap.min.child.next.child.next
        assert n.key == 46
        assert n.parent.mark is False
        heap.decrease_key(n, 15)
        assert n.key == 15
        assert heap.min.child.next.mark is True
        assert len(list(heap.root_nodes)) == 4
        n = heap.min.child.next.child.child
        assert n.key == 35
        assert n.parent.mark is True
        assert n.parent.parent.mark is True
        assert n.parent.parent.parent.mark is False
        assert n.parent.parent.parent.key == 7
        heap.decrease_key(n, 5)
        assert len(list(heap.root_nodes)) == 7
        assert heap.min == n

    def test_delete(self):
        """Test delete using lecture slide example."""
        heap = heap_from_slides()
        heap.min.prev.insert(node.Node(21))
        heap.size += 1
        heap.extract_min()
        n = heap.min.child.next.child.next
        assert n.key == 46
        assert n.parent.mark is False
        heap.decrease_key(n, 15)
        assert n.key == 15
        assert heap.min.child.next.mark is True
        assert len(list(heap.root_nodes)) == 4
        n = heap.min.child.next.child.child
        assert n.key == 35
        assert n.parent.mark is True
        assert n.parent.parent.mark is True
        assert n.parent.parent.parent.mark is False
        assert n.parent.parent.parent.key == 7
        assert heap.size == 14
        heap.delete(n)
        assert heap.size == 13
