"""
FIT3155 - Lab 10 - Task 3
"""

import heapq
from collections import Counter

import elias_decoder
import elias_encoder


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


def encode_header(code: str) -> str:
    res = unique_chars(code)
    # Total number of unique characters
    result = elias_encoder.encode_single_value(len(res))
    for val in res:
        # Frequency of each character
        result += elias_encoder.encode_single_value(res[val])
        # ASCII code of character padded to 3 digits.
        result += "{0:0=3d}".format(ord(val))
    # Total number of characters in the input file.
    result += elias_encoder.encode_single_value(len(code))
    return result


def encoded_values(code: str) -> (dict, Node):
    unique = unique_chars(code)
    heap = []
    for val in unique:
        node = Node(val, unique[val])
        heapq.heappush(heap, node)
    root = heap[0]
    while len(heap) > 1:
        min1: Node = heapq.heappop(heap)
        min2: Node = heapq.heappop(heap)
        new_node = Node(min1.char + min2.char, min1.count + min2.count)
        new_node.left = min1
        new_node.right = min2
        root = new_node

        heapq.heappush(heap, new_node)

    # Traverse
    bin_representation = {}
    calculate_string(root, "", bin_representation)
    return bin_representation, root


def encode(code):
    bin_representation, root = encoded_values(code)
    # Traverse
    calculate_string(root, "", bin_representation)
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
    # Calculate no of unique and remove from code.
    no_of_unique = elias_decoder.decode_single_value(code)
    no_of_unique_encoded = elias_encoder.encode_single_value(no_of_unique)
    code = code[len(no_of_unique_encoded) :]

    frequencies = {}
    for i in range(no_of_unique):
        freq = elias_decoder.decode_single_value(code)
        freq_encoded = elias_encoder.encode_single_value(freq)
        code = code[len(freq_encoded) :]
        char = chr(int(code[0:3]))
        code = code[3:]
        frequencies[char] = freq

    total_chars = elias_decoder.decode_single_value(code)
    total_chars_encoded = elias_encoder.encode_single_value(total_chars)
    code = code[len(total_chars_encoded) :]

    heap = []
    for val in frequencies:
        node = Node(val, frequencies[val])
        heapq.heappush(heap, node)
    root = heap[0]

    while len(heap) > 1:
        min1: Node = heapq.heappop(heap)
        min2: Node = heapq.heappop(heap)
        new_node = Node(min1.char + min2.char, min1.count + min2.count)
        new_node.left = min1
        new_node.right = min2
        root = new_node

        heapq.heappush(heap, new_node)

    result = ""
    for i in range(total_chars):
        res = search_for_char(root, "", code, -1)
        result += res[1]
        code = code[len(res[0]) :]

    return result


def search_for_char(node: Node, string: str, codeword: str, index_to_search: int):
    if node.left is None and node.right is None:
        return string, node.char
    index_to_search += 1
    if codeword[index_to_search] == "0":
        return search_for_char(node.left, string + "0", codeword, index_to_search)
    else:
        return search_for_char(node.right, string + "1", codeword, index_to_search)
