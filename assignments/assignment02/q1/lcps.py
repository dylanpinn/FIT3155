#!/usr/bin/env python3

"""Lowest Common Prefix Common to the suffixes.

FIT3155 - Assignment 2.
Dylan Pinn 24160547
"""
import sys
from typing import List, Optional, Union

ALPHABET_SIZE = 256


class EndOfPathException(Exception):
    pass


class RootNode:
    """The Root Node in the suffix tree."""

    edges: List[Optional["Edge"]]

    def __init__(self):
        self.edges = [None] * ALPHABET_SIZE

    def add_edge(self, edge: "Edge", char: str):
        """Add an edge to the node."""
        self.edges[ord(char)] = edge

    def search(self, char: str) -> Optional["Edge"]:
        """Search for the edge for the node."""
        return self.edges[ord(char)]

    def __repr__(self):
        return "RootNode"

    @property
    def filtered_edges(self):
        """Get a list of edges that have values."""
        return list(filter(lambda x: isinstance(x, Edge), self.edges))


class Node(RootNode):
    """A node in the tree that can have an index and suffix link."""

    edge: "Edge"

    def __init__(
        self, index: int = None, link: Union["Node", "RootNode"] = None
    ):
        super().__init__()
        self.index = index
        self.link = link

    def __repr__(self):
        return f"Node({self.index})"


class Edge:
    """An edge in the suffix tree."""

    def __init__(
        self,
        start: int,
        end: Union[int, "GlobalEnd"],
        destination: "Node",
        tree: "SuffixTree",
        beginning: Union["RootNode", "Node"],
    ):
        self.start = start
        self.end = end
        self.destination = destination
        self.beginning = beginning
        self.tree = tree

    def split(self, index: int) -> "Node":
        """Split the edge at an index to create a new internal node
        and new edge to the previous end.
        """
        internal_node = Node(None, self.tree.root)
        internal_node.edge = self
        new_edge = Edge(
            self.start + index,
            self.end,
            self.destination,
            self.tree,
            internal_node,
        )
        self.destination.edge = new_edge
        self.end = self.start + index - 1
        self.destination = internal_node
        internal_node.add_edge(new_edge, self.tree.text[self.start + index])

        return internal_node

    @property
    def label(self):
        """Show the label for the edge."""
        return self.tree.text[self.start : int(self.end) + 1]

    def __len__(self):
        return int(self.end) - self.start

    def __repr__(self):
        return (
            f"Edge({self.start},{self.end})[{self.label}] -> "
            f"N({self.destination.index if self.destination else None})"
        )


class GlobalEnd:
    def __init__(self):
        self.end = -1

    def increment(self):
        """Increment the global end value."""
        self.end += 1

    def __repr__(self):
        return "GlobalEnd(%d)" % self.end

    def __int__(self):
        return self.end


class SuffixTree:
    def __init__(self, text: str):
        self.n = len(text)
        self.text = text
        self.root = RootNode()
        self.current_end = GlobalEnd()
        self.active_length = 0
        self.active_node = self.root
        self.active_edge = -1
        self.remaining = 0
        self.build()

    def add_new_edge_to_active_node(self, start: int):
        node = Node(start)
        edge = Edge(start, self.current_end, node, self, self.active_node)
        node.edge = edge
        self.active_node.add_edge(edge, self.text[start])

    def build(self):
        """Build suffix tree using Ukkonen's algorithm."""
        for i in range(0, self.n):
            self._phase(i)
        self.update_indices(self.root, 0, self.n)

    def _phase(self, i: int):
        """Do work for each phase in building the tree."""
        self.remaining += 1
        self.current_end.increment()  # Rule 1 Extension.
        last_internal_node = None

        while self.remaining > 0:
            if self.active_length == 0:
                # check if path from root with self.text[i]
                edge = self.active_node.search(self.text[i])
                # Rule 2 Extension
                if edge is None:
                    self.add_new_edge_to_active_node(i)
                    self.remaining -= 1
                else:
                    self.active_edge = edge.start
                    self.active_length += 1
                    break  # Phase 3: Show stopper - end phase
            else:
                try:
                    next_char = self.next_char(i)
                    # check from active point if next character is self.text[i]
                    if next_char == self.text[i]:
                        edge = self.active_point()
                        # if it is past next node then update
                        if len(edge) < self.active_length:
                            # Update active edge
                            self.active_node = edge.destination
                            self.active_length = self.active_length - len(edge)
                            self.active_edge = self.active_node.search(  # type: ignore
                                self.text[i]
                            ).start

                        else:
                            self.active_length += 1
                        break  # Phase 3: Show stopper - end phase
                    else:
                        # Rule 2: Split edge with new internal node and create new edge

                        edge = self.active_point()
                        internal_node = edge.split(self.active_length)
                        leaf_node = Node(i, None)
                        new_edge = Edge(
                            i,
                            self.current_end,
                            leaf_node,
                            self,
                            edge.destination,
                        )
                        leaf_node.edge = new_edge
                        edge.destination.add_edge(new_edge, self.text[i])
                        self.remaining -= 1
                        if self.active_node != self.root:
                            self.active_node = (
                                self.active_node.link  # type: ignore
                            )
                        else:
                            self.active_length -= 1
                            self.active_edge += 1

                        # Create Suffix Link
                        if last_internal_node is not None:
                            last_internal_node.link = internal_node

                        last_internal_node = internal_node

                except EndOfPathException:
                    # Rule 2: Add new edge to node
                    node = self.active_node
                    edge = node.search(self.text[self.active_edge])
                    leaf_node = Node(i, None)
                    new_edge = Edge(
                        i,
                        self.current_end,
                        leaf_node,
                        self,
                        edge.destination,  # type: ignore
                    )
                    leaf_node.edge = new_edge
                    edge.destination.add_edge(  # type:ignore
                        new_edge, self.text[i]
                    )
                    self.remaining -= 1
                    if self.active_node != self.root:
                        self.active_node = (
                            self.active_node.link  # type:ignore
                        )
                    else:
                        self.active_length -= 1
                        self.active_edge += 1

                    # Create Suffix Link
                    if last_internal_node is not None:
                        last_internal_node.link = node

                    last_internal_node = node  # type: ignore

    def next_char(self, index: int) -> Optional[str]:
        """Return the next character in the active edge from the tree's active point."""
        edge = self.active_point()
        # In edge path
        if len(edge) >= self.active_length:
            return self.text[edge.start + self.active_length]
        else:
            if len(edge) + 1 == self.active_length:
                if edge.destination.search(self.text[index]) is not None:
                    return self.text[index]
                raise EndOfPathException
            else:
                # not in current edge
                # update active node, edge and length.
                self.active_node = edge.destination
                self.active_length = self.active_length - len(edge) - 1
                self.active_edge = self.active_edge + len(edge) + 1
                return self.next_char(index)

    def active_point(self) -> "Edge":
        """Return the active edge."""
        return self.active_node.search(  # type: ignore
            self.text[self.active_edge]
        )

    def update_indices(self, root: "RootNode", value: int, size: int):
        """Use DFS Traversal to update all of the leaf indices."""
        if root is None:
            return

        edges = root.filtered_edges
        for edge in edges:
            self._update_index(edge, value, size)

    def _update_index(self, edge: "Edge", value: int, size: int):
        """"Update the index for an edge."""
        value += len(edge) + 1
        destination = edge.destination
        if len(destination.filtered_edges) == 0:
            destination.index = size - value
        else:
            for child_edge in destination.filtered_edges:
                self._update_index(child_edge, value, size)

    def find_lcps(self, i: int, j: int, index_offset: int = 1) -> int:
        """Find longest prefix common to the suffixes starting at position i and j."""
        result = 0
        j_edge, i_edge = None, None
        if i + index_offset > self.n or j + index_offset > self.n:
            return result
        # find each index node
        for edge in self.root.filtered_edges:
            if i_edge is not None:
                break
            i_edge = self._dfs_for_lcps(edge, i, index_offset)
        for edge in self.root.filtered_edges:
            if j_edge is not None:
                break
            j_edge = self._dfs_for_lcps(edge, j, index_offset)
        # find common ancestor to both
        i_parent, j_parent = i_edge.beginning, j_edge.beginning  # type: ignore
        while i_parent != j_parent:
            if i_parent != self.root:
                i_parent = i_parent.edge.beginning
            if j_parent != self.root:
                j_parent = j_parent.edge.beginning

        while i_parent is not self.root:
            result += len(i_parent.edge) + 1
            i_parent = i_parent.edge.beginning

        # count from common ancestor to root
        return result

    def _dfs_for_lcps(self, edge: "Edge", index: int, index_offset: int):
        if edge.destination.index == index - index_offset:
            return edge

        for child_edge in edge.destination.filtered_edges:
            leaf = self._dfs_for_lcps(child_edge, index, index_offset)
            if leaf is not None:
                return leaf


if __name__ == "__main__":
    # executed directly
    input_text = open(sys.argv[1], "r")
    pairs_file = open(sys.argv[2], "r")
    text = input_text.read()
    text = text.rstrip() + "$"
    tree = SuffixTree(text)

    output_file = open("output_lcps.txt", "w")
    line = pairs_file.readline()
    while line:
        line = line.rstrip()
        values = line.split()
        if len(values) == 2:
            i, j = values[0], values[1]
            res = tree.find_lcps(int(i), int(j), 1)
            output_file.write(f"{i} {j} {res}\n")

        line = pairs_file.readline()

    output_file.close()
