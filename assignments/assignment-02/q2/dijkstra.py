#!/usr/bin/env python3

"""Dijkstra shortest path using Fibonacci Heap."""
import math
import os
import sys

from min_heap import MinHeap


class Graph:
    """Graph represented by Min Heaps."""

    def __init__(self, size):
        self.vertices = [[] for _ in range(size + 1)]

    def add_edge(self, source, dest, weight):
        """Add a weighted edge to the graph."""
        self.vertices[source].append([dest, weight])

    def shortest_path(self, source, target, exit_early=True):
        """Find the shortest path from source to target."""
        # Keep track of state and heap indices
        vertices = [-2] * len(self.vertices)
        discovered = MinHeap()
        discovered.insert([source, 0, None])
        vertices[0] = 0
        finalised = []
        # keep track of the min distance for a vertex
        min_distances = [math.inf] * len(self.vertices)
        while not discovered.is_empty():
            # get the vertex from the discovered list with the smallest
            # distance
            vertex = discovered.pop_min()
            v = vertex[0]
            v_dist = vertex[1]
            # finalised vertices are marked with index in finalised > 0
            # discovered vertices are marked with -1
            if vertices[v] < 0:
                # not finalised
                for edge in self.vertices[v]:
                    u, w = edge[0], edge[1]
                    dist = v_dist + w
                    if vertices[u] < 0 and (vertices[u] == -2 or min_distances[u] > dist):
                        discovered.insert((u, dist, v))
                        vertices[u] = -1
                        min_distances[u] = dist

                # move v from discovered to finalised
                add_to_finalised = True
                for item in finalised:
                    if item[0] == v:
                        add_to_finalised = False
                        break
                if add_to_finalised:
                    finalised.append(vertex)
                    vertices[v] = len(finalised) - 1
                if v == target and exit_early:
                    break

        return finalised, vertices


def file_in_current_dir(filename: str) -> str:
    """Load file from current directory."""
    path_to_current_file = os.path.realpath(__file__)
    current_directory = os.path.split(path_to_current_file)[0]
    return os.path.join(current_directory, filename)


def build_graph_from_edge_file(filename):
    """Get edges from file."""
    filename = file_in_current_dir(filename)
    file = open(filename)
    for idx, line in enumerate(file):
        line = line.strip()
        if idx == 0:
            # First line is the max ID of any edge.
            graph = Graph(int(line))
        else:
            source, dest, distance = line.split(' ', 2)
            graph.add_edge(int(source), int(dest), int(distance))
            graph.add_edge(int(dest), int(source), int(distance))
    return graph


if __name__ == "__main__":
    graph = build_graph_from_edge_file(sys.argv[1])
    start_dist, _ = graph.shortest_path(1, 1, False)

    output_file = open('output_dijkstra.txt', 'w')

    start_dist.sort(key=lambda x: x[0])

    for i in range(len(start_dist)):
        output_file.write(f'{start_dist[i][0]}  {start_dist[i][1]}\n')

    output_file.close()
