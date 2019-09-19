"""Test Fibonacci Heap implementation."""

import pytest

import fib_heap


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

    @pytest.mark.skip(reason="TODO: Need to complete implementation")
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
