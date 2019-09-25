"""Lowest Common Prefix Common to the suffixes."""

from typing import List, Optional

ALPHABET_SIZE = 256


def naive_implementation():
    """Solution using naive inefficient algorithm."""
    # Generate all suffixes of a given text.
    # Consider all suffixes as individual words and build a compressed trie.
    # - insert largest to smallest in tree
    # - label each leaf with the starting point of the corresponding suffix

    # Pattern Search
    # - starting from the first character of the pattern and root of suffix tree, do following for every character
    # -- for the current character of the pattern, if there is an edge from teh current node of suffix tree,
    # --  follow the edge
    # --- if there is no edge, then pattern doesn't exist and return.
    # --- if all of the characters of pattern have been processed, then pattern is found.

    pass


def generate_suffixes(text: str) -> List[str]:
    """Generate a list of suffixes for a given text."""
    n = len(text)
    suffixes = []
    for i in range(0, n):
        suffixes.append(text[i:n])
    return suffixes


class Node:
    """A node in the suffix tree."""
    edges: List[Optional['Edge']]

    def __init__(self, suffix_index: Optional[int]):
        self.suffix_index = suffix_index
        self.edges = [None] * ALPHABET_SIZE

    def add_edge(self, edge: 'Edge', char: str):
        """Add an edge to the node."""
        self.edges[ord(char)] = edge
        # self.edges.append(edge)

    def search(self, char: str):
        """Search for the edge for the node."""
        return self.edges[ord(char)]

    def __repr__(self):
        return "Node"

    def _filtered_edges(self):
        return list(filter(None, self.edges))


class Edge:
    """An edge in the suffix tree."""

    def __init__(self, start, end, destination: 'Node'):
        self.start = start
        self.end = end
        self.destination = destination

    # def __init__(self, start, end):
    #     self.start = start
    #     self.end = end
    #     # self.destination = destination

    # def __repr__(self):
    #     return 'Edge(%d, %d)' % (self.start, self.end if isinstance(self.end, int) else self.end.end)


# class CurrentEnd:
#     def __init__(self):
#         self.end = -1
#
#     def increment(self):
#         """Increment the current end value."""
#         self.end += 1
#
#     def __repr__(self):
#         return 'CurrentEnd(%d)' % self.end


class SuffixTree:
    def __init__(self, text):
        self.n = len(text)
        self.text = text
        self.root = Node(None)
        self.build()

    def build(self):
        """Build a suffix tree using provided text."""
        for i in range(0, self.n):
            phase = i + 1
            print('phase ', phase)
            for j in range(0, i + 1):
                extension = j + 1
                print('extension ', extension)
                # begin suffix extension j
                # find end of the path from root denoting str[j..i] in the current state of the suffix tree

                # Tree traversal return edge

                edge = self.root.search(self.text[j])

                # apply one of the three suffix extension rules

                # Rule 2: Edge not found; insert at root
                if edge is None:
                    self.root.add_edge(Edge(j, i, Node(j)), self.text[j])
                # Rule 1: Ends at a leaf, adjust edge to extend extra character.
                elif i - 1 == edge.end:
                    edge.end = i
                elif edge.start < i - 1 < edge.end:
                    # Rule 2: Rule 2: In tree but next value is not in path.
                    # if next character is not same as current character then create new internal node and split
                    print('')
                    # Rule 3: Within path, do nothing.
                    pass
                else:
                    # raise Exception
                    pass
                print('next')

            #  end of extension step j
            # end of phase i+ 1

            # self.insert(self.text[i], i)
            # self.insert(text[i:self.n], i, self.n)

    # def insert(self, suffix: str, start_index: int):
    #     """Insert a prefix into the Tree."""
    #     self.current_end.increment()
    #
    #     # Step 1-3: Doesn't match. Add to root node
    #     if start_index < 3:
    #         edge = Edge(start_index, self.current_end)
    #         self.active_point[0].add_edge(edge)
    #         self.remainder = 1
    #
    #     # Step 4:
    #     if start_index == 3:
    #         self.active_point = (self.root, 'a', 1)
    #         self.remainder += 1
    #     # Step 5
    #     if start_index == 4:
    #         self.active_point = (self.root, 'a', 2)
    #         self.remainder += 1
    #     # Step 6
    #     if start_index == 5:
    #         print('step 6')

    # def insert(self, suffix: str, start_index: int, end_index: int):
    #     """
    #     - Start at the root of Ni
    #     - Find the longest path from the root which matches a prefix of S[i+1..m]$
    #     - Match ends either at the node (say w) or in the middle of an edge [say (u, v)].
    #     - If it is in the middle of an edge (u, v), break the edge (u, v) into two edges by inserting a new node w just
    #     after the last character on the edge that matched a character in S[i+l..m] and just before the first character
    #     on the edge that mismatched. The new edge (u, w) is labelled with the part of the (u, v) label that matched
    #     with S[i+1..m], and the new edge (w, v) is labelled with the remaining part of the (u, v) label.
    #     - Create a new edge (w, i+1) from w to a new leaf labelled i+1 and it labels the new edge with the unmatched
    #     part of suffix S[i+1..m]
    #     """
    #     # Find the longest path from the root which matches a prefix of S[i+1..m]$
    #
    #     end_node = Node(start_index)
    #     edge = Edge(start_index, end_index, end_node)
    #     self.root.add_edge(edge)
    #     print(suffix)


def generate_suffix_tree(text: str):
    """Naive implementation to generate suffix tree."""
    tree = SuffixTree(text)

    # raise

    return tree
