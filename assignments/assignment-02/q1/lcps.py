"""Lowest Common Prefix Common to the suffixes."""

from typing import List, Optional, Union

ALPHABET_SIZE = 256


def generate_suffixes(text: str) -> List[str]:
    """Generate a list of suffixes for a given text."""
    n = len(text)
    suffixes = []
    for i in range(0, n):
        suffixes.append(text[i:n])
    return suffixes


class RootNode:
    """A node in the suffix tree."""
    edges: List[Optional['Edge']]

    def __init__(self):
        self.edges = [None] * ALPHABET_SIZE

    def add_edge(self, edge: 'Edge', char: str):
        """Add an edge to the node."""
        self.edges[ord(char)] = edge

    def search(self, char: str) -> Optional['Edge']:
        """Search for the edge for the node."""
        return self.edges[ord(char)]

    def __repr__(self):
        return 'RootNode'

    @property
    def filtered_edges(self):
        return list(filter(lambda x: isinstance(x, Edge), self.edges))


class Node(RootNode):
    def __init__(self, index: int = None, link: Union['Node', 'RootNode'] = None):
        super().__init__()
        self.index = index
        self.link = link

    def __repr__(self):
        return f'Node({self.index})'


class Edge:
    """An edge in the suffix tree."""

    def __init__(self, start: int, end: Union[int, 'GlobalEnd'], destination: 'Node', tree: 'SuffixTree'):
        self.start = start
        self.end = end
        self.destination = destination
        self.tree = tree

    def split(self, index: int) -> 'Node':
        internal_node = Node(None, self.tree.root)
        new_edge = Edge(self.start + index, self.end, self.destination, self.tree)
        # if single character split then self.end = index else index - 1
        self.end = self.start if index == 1 else index - 1
        self.destination = internal_node
        internal_node.add_edge(new_edge, self.tree.text[self.start + index])

        return internal_node

    # def __init__(self, start, end):
    #     self.start = start
    #     self.end = end
    #     # self.destination = destination

    @property
    def label(self):
        return self.tree.text[self.start:int(self.end) + 1]

    def __len__(self):
        return int(self.end) - self.start

    def __repr__(self):
        return f'Edge({self.start},{self.end})[{self.label}] -> ' \
               f'N({self.destination.index if self.destination else None})'


class GlobalEnd:
    def __init__(self):
        self.end = -1

    def increment(self):
        """Increment the global end value."""
        self.end += 1

    def __repr__(self):
        return 'GlobalEnd(%d)' % self.end

    def __int__(self):
        return self.end


class SuffixTree:
    def __init__(self, text):
        self.n = len(text)
        self.text = text
        self.root = RootNode()
        # active_point = (active_node, active_edge, active_length)
        # self.active_point = (self.root, -1, 0)
        self.current_end = GlobalEnd()
        self.active_length = 0
        self.active_edge = -1
        self.active_node = self.root
        self.remaining = 0
        self.build2()

    def add_new_edge_to_active_node(self, start):
        node = Node(start)
        edge = Edge(start, self.current_end, node, self)
        self.active_node.add_edge(edge, self.text[start])

    def build2(self):
        for i in range(0, self.n):
            self._phase(i)

    def _phase(self, i):
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
                next_char = self.next_char(i)
                # check from active point if next character is self.text[i]
                if next_char == self.text[i]:
                    edge = self.active_point()
                    # if it is past next node then update
                    if len(edge) < self.active_length:
                        # Update active edge
                        # active.activeNode = node;
                        # active.activeLength = active.activeLength - diff(node);
                        # active.activeEdge = node.child[input[index]].start;
                        print('TODO')
                    else:
                        self.active_length += 1
                    break  # Phase 3: Show stopper - end phase
                elif next_char is None:
                    # TODO: Remove this branch.
                    next_node = self.active_edge.destination
                    edge = next_node.search(self.text[self.active_length])
                    # Rule 2: Create new edge from node
                    if edge is None:
                        print('')
                    else:
                        # Rule 3: Show stopper - end phase
                        self.active_node = self.active_edge.destination
                        self.active_length = 1
                        self.active_edge_idx = edge.start
                        self.active_edge = edge
                        break
                else:
                    # Rule 2: Split edge with new internal node and create new edge

                    # get node
                    # old_start = node.start
                    # node.start = node.start + self.active_length
                    # new_node = Node(old_start, old_start + active_length - 1)

                    # create new leaf node
                    # new_leaf_node = Node(i, this.end)

                    # set internal nodes child as old node and new leaf node.
                    # newInternalNode.child[input[newInternalNode.start + active.activeLength]] = node;
                    # newInternalNode.child[input[i]] = newLeafNode;
                    # newInternalNode.index = -1;
                    # active.activeNode.child[input[newInternalNode.start]] = newInternalNode;

                    # Create Suffix Link
                    # if last_internal_node is not None:
                    #     last_internal_node.link = internal_node

                    # last_internal_node = internal_node

                    # if active node is not root then follow suffix link
                    # if self.active_node != self.root:
                    #     self.active_node = self.active_node.link
                    # else:
                    #     self.active_length -= 1
                    #     self.active_edge_idx += 1
                    #     self.active_edge = self.active_node.search(self.text[self.active_edge_idx])

                    # self.remaining -= 1

                    edge = self.active_point()

                    internal_node = edge.split(self.active_length)
                    # TODO: Check this node index.
                    leaf_node = Node(i, self.root)
                    new_edge = Edge(i, self.current_end, leaf_node, self)
                    edge.destination.add_edge(new_edge, self.text[i])
                    self.remaining -= 1
                    if self.active_node != self.root:
                        self.active_node = self.active_node.link
                    else:
                        self.active_length -= 1
                        self.active_edge += 1

                    # Create Suffix Link
                    if last_internal_node is not None:
                        last_internal_node.link = internal_node

                    last_internal_node = internal_node

    def next_char(self, index: int) -> str:
        """Return the next character in the active edge from the tree's active point."""
        edge = self.active_point()
        # In edge path
        if len(edge) >= self.active_length:
            return self.text[edge.start + self.active_length]
        else:
            if self.active_node == self.root:
                # not in current edge
                self.active_node = edge.destination
                new_edge = self.active_node.search(self.text[index])
                # update active node, edge and length and search again.
                if new_edge is not None:
                    self.active_length = self.active_length - len(edge) - 1
                    self.active_edge = new_edge.start
                    return self.text[self.active_point().start]
                    # return self.next_char(index)
                else:
                    print('')
            else:
                return self.text[edge.start + self.active_length]

    def active_point(self) -> 'Edge':
        return self.active_node.search(self.text[self.active_edge])


def generate_suffix_tree(text: str):
    """Generate suffix tree."""
    tree = SuffixTree(text)

    return tree
