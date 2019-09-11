"""Test Fibonacci Heap implementation."""


from fib_heap import FibonacciHeap


class TestFibonacciHeap:
    def test_initial_min(self):
        """Initial min should be nil."""
        heap = FibonacciHeap()
        assert heap.min is None

    def test_initial_size(self):
        """Initial size should be 0."""
        heap = FibonacciHeap()
        assert heap.size == 0

    def test_insert_empty(self):
        """Test inserting into an empty Heap."""
        heap = FibonacciHeap()
        heap.insert(1)
        assert heap.min.key == 1
        assert heap.size == 1

    def test_insert(self):
        """Test inserting ino a non-empty Heap."""
        heap = FibonacciHeap()
        heap.insert(10)
        heap.insert(5)
        assert heap.min.key == 5
        assert heap.root_nodes.size == 2
        assert heap.size == 2
