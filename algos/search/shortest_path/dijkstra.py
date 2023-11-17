import math

from algos.graph import WeightedDirectedEdge, WeightedDirectedGraph
from algos.priority_queue import PriorityQueue
from algos.stack import Stack
from typing import List


# ------------------------- Dijkstra's Algorithm ---------------------------- #
# Shortest Path Search
# ----------------------------------------------------------------------- #
class DijkstraSP:
    edge_to: List[WeightedDirectedEdge]
    dist_to: List[float]
    pq: PriorityQueue

    def __init__(self, graph: WeightedDirectedGraph, s: int):
        self.edge_to = [WeightedDirectedEdge] * graph.vertices()
        self.dist_to = [float] * graph.vertices()
        self.pq = [float] * graph.vertices()

        n = graph.vertices()
        for i in range(0, n):
            self.dist_to[i] = math.inf

        self.dist_to[s] = 0.0

        self.pq.insert(s, 0.0)

        while not self.pq.is_empty():
            self.relax(graph, self.pq.delete(0))

    def relax(self, graph: WeightedDirectedGraph, v: int):
        e: WeightedDirectedEdge
        for e in graph.adj(v):
            u = e.vertex_to()
            if self.dist_to[u] > self.dist_to[v] + e.get_weight():
                self.dist_to[u] = self.dist_to[v] + e.get_weight()
                self.edge_to[u] = e

                if self.pq.contains(u):
                    self.pq.change(u, self.dist_to[u])
                else:
                    self.pq.insert(u, self.dist_to[u])

    def distance_to(self, v: int):
        return self.dist_to[v]

    def has_path_to(self, v: int) -> bool:
        return self.dist_to[v] < math.inf

    def path_to(self, v: int):
        if not self.has_path_to(v):
            return None

        path = Stack()
        e: WeightedDirectedEdge = self.edge_to[v]

        while e is not None:
            path.push(e)
            e = self.edge_to[e.vertex_from()]

        return path


class DijkstraAllPairsSP:
    all: List[DijkstraSP]

    def __init__(self, graph: WeightedDirectedGraph):
        n = graph.vertices()
        self.all = [DijkstraSP] * n

        for i in range(0, n):
            self.all[i] = DijkstraSP(graph, i)

    def path(self, s: int, t: int):
        return self.all[s].path_to(t)

    def distance_to(self, s: int, t: int):
        return self.all[s].distance_to(t)
