"""Lowest Common Prefix Common to the suffixes."""

from typing import List, Optional

ALPHABET_SIZE = 256


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

    def __init__(self, index: Optional[int] = None):
        self.index = index
        self.edges = [None] * ALPHABET_SIZE

    def add_edge(self, edge: 'Edge', char: str):
        """Add an edge to the node."""
        self.edges[ord(char)] = edge
        # self.edges.append(edge)

    def search(self, char: str):
        """Search for the edge for the node."""
        return self.edges[ord(char)]

    def __repr__(self):
        return f'Node({self.index})'

    @property
    def _filtered_edges(self):
        return list(filter(None, self.edges))


class Edge:
    """An edge in the suffix tree."""

    def __init__(self, label: str, destination: 'Node'):
        self.label = label
        self.destination = destination

    def split(self, label: str) -> 'Edge':
        remaining_label = self.label[len(label):]
        internal_node = Node()
        new_edge = Edge(remaining_label, self.destination)
        self.label = label
        self.destination = internal_node
        internal_node.add_edge(new_edge, remaining_label[0])

        return new_edge

    # def __init__(self, start, end):
    #     self.start = start
    #     self.end = end
    #     # self.destination = destination

    def __repr__(self):
        return f'Edge({self.label}) -> N({self.destination.index if self.destination else None})'


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

                search_node = self.root

                # Tree traversal return edge

                edge = search_node.search(self.text[j])

                path = self.text[j:i + 1]

                # apply one of the three suffix extension rules

                # Rule 2: Edge not found; insert at root
                if edge is None:
                    node = Node(j)
                    edge = Edge(path, node)
                    self.root.add_edge(edge, self.text[j])
                else:
                    # Do some traversal if required
                    while edge is not None and len(path) > len(edge.label) + 1:
                        path: str = path[path.find(edge.label) + len(edge.label):]
                        edge = edge.destination.search(path[0])

                    if edge is None:
                        # Handle this
                        raise Exception

                    # Rule 1: text[j..i-1] ends at a leaf
                    if path[:-1] == edge.label and edge.destination.index is not None:
                        edge.label = path
                    elif edge.label.startswith(path):
                        # Rule 3: Within path, do nothing.
                        pass
                    else:
                        # if next value is an edge go to it
                        if len(edge.label) + 1 == len(path):
                            path: str = path[path.find(edge.label) + len(edge.label):]
                            edge = edge.destination.search(path[-1])
                            if edge is None:
                                # Handle this
                                raise Exception
                            else:
                                if path[:-1] == edge.label and edge.destination.index is not None:
                                    edge.label = path
                                elif edge.label.startswith(path):
                                    # Rule 3: Within path, do nothing.
                                    pass
                                else:
                                    raise Exception
                        else:
                            index_of_mismatch = -1
                            if len(path) < len(edge.label):
                                for n in range(0, len(path)):
                                    if path[n] != edge.label[n]:
                                        index_of_mismatch = n
                                        break
                            else:
                                # Handle this
                                raise Exception

                            # Rule 2: Rule 2: In tree but next value is not in path.
                            edge.split(edge.label[0:index_of_mismatch])
                            edge.destination.add_edge(Edge(path[-1], Node(j)), path[-1])

            #  end of extension step j
            # end of phase i+ 1

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
