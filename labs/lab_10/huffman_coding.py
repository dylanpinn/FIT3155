"""
FIT3155 - Lab 10 - Task 3
"""

import heapq
from collections import Counter


class Node:
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.count < other.count


def unique_chars(code: str) -> Counter:
    return Counter(code)


def encode(code):
    unique = unique_chars(code)
    heap = []
    for val in unique:
        node = Node(val, unique[val])
        heapq.heappush(heap, node)
    while len(heap) > 1:
        min1: Node = heapq.heappop(heap)
        min2: Node = heapq.heappop(heap)
        new_node = Node(min1.char + min2.char, min1.count + min2.count)
        new_node.left = min1
        new_node.right = min2

        heapq.heappush(heap, new_node)

    # Traverse
    bin_representation = {}
    calculate_string(heap[0], "", bin_representation)
    huffman_code = ""
    for i in range(len(code)):
        huffman_code += bin_representation[code[i]]
    return huffman_code


def calculate_string(node: Node, string: str, dict: dict):
    if node.left is None and node.right is None:
        dict[node.char] = string
        return

    calculate_string(node.left, string + "0", dict)
    calculate_string(node.right, string + "1", dict)


def decode(code):
    pass
