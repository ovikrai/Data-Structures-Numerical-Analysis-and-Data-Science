import math

from algos.graph import Graph
from algos.bag import Bag


# ------------------------- Dijkstra's Algorithm ---------------------------- #
# Shortest Path Search
# ----------------------------------------------------------------------- #
# TODO: CHANGE DEGREE FOR THE NEW IMPLEMENTATION OF GRAPH
class Dijkstra(object):
    vertex_count: int
    source_vertex: int
    dist: list
    prev: list
    Q: Bag

    def __init__(self, G: Graph, source_vertex: int):
        self.source_vertex = source_vertex
        self.vertex_count = G.vertex_count()

        for i in range(0, self.vertex_count):
            self.dist[i] = math.inf
            self.prev[i] = False
            # self.Q.add()
        self.dist[source_vertex] = 0

        while not self.Q.is_empty():
            u = self.min_dist(self.dist, self.prev)
            self.Q.remove(u)
            self.prev[u] = True

            for v in range(0, self.vertex_count):
                if G.degree(v) > 0 and \
                        self.prev[v] is False and \
                        self.dist[v] > self.dist[u] + G.degree(v):
                    self.dist[v] = self.dist[u] + G.degree(v)

    def min_dist(self, dist, prev):
        min_dist = math.inf
        min_index = 0

        for v in range(0, self.vertex_count):
            if dist[v] < min_dist and prev[v] is False:
                min_dist = dist[v]
                min_index = v

        return min_index
