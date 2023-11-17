import math

from algos.queue import Queue
from algos.priority_queue import PriorityQueue
from algos.graph import WeightedEdge, WeightedGraph


# ------------------------- Prim's Minimum Spanning Tree ---------------------------- #
# Search in a graph
#
# Runtime T(n):
#   Best: T(n) ~ c
#   Average: T(n) ~ 1/2 * (|V| + |E|)
#   Worst: T(n) ~ |V| + |E|
#
# Asymptotically Analysis (Big O):
#   Best: T(n) = O(1)
#   Average: T(n) = O(|V| + |E|)
#   Worst: T(n) = O(|V| + |E|)
#
# ----------------------------------------------------------------------- #

class PrimLazyMST:
    marked: list
    mst: Queue
    pq: PriorityQueue

    def __init__(self, graph: WeightedGraph):
        self.pq = PriorityQueue(max_n=graph.vertices())
        self.marked = self.marked = [bool] * graph.vertices()
        self.mst = Queue()

        self.visit(graph, 0)
        while not self.pq.is_empty():
            e: WeightedEdge = self.pq.delete(0)
            v = e.either()
            u = e.other(v)

            if self.marked[v] and self.marked[u]:
                continue

            self.mst.enqueue(e)

            if not self.marked[v]:
                self.visit(graph, v)

            if not self.marked[u]:
                self.visit(graph, u)

    def visit(self, graph: WeightedGraph, v: int):
        self.marked[v] = True
        for e in graph.adj:
            if not self.marked[e.other(v)]:
                self.pq.insert(v, e)

    def get_edges(self):
        return self.mst


class PrimEagerMST:
    edge_to: list
    dist_to: list
    marked: list
    pq: PriorityQueue

    def __init__(self, graph: WeightedGraph):
        self.edge_to = [WeightedEdge] * graph.vertices()
        self.dist_to = [float] * graph.vertices()
        self.marked = [bool] * graph.vertices()

        for v in range(0, graph.vertices()):
            self.dist_to[v] = math.inf

        self.pq = PriorityQueue(max_n=graph.vertices())
        self.dist_to[0] = 0.0
        self.pq.insert(0, 0.0)
        while not self.pq.is_empty():
            self.visit(graph, self.pq.delete(0))

    def visit(self, graph: WeightedGraph, v: int):
        self.marked[v] = True

        for e in graph.adj:
            u = e.other(v)

            if self.marked[u]:
                continue

            if e.get_weight() < self.dist_to[u]:
                self.edge_to[u] = e
                self.dist_to[u] = e.get_weight()

                if self.pq.contains(u):
                    self.pq.change(u, self.dist_to[u])
                else:
                    self.pq.insert(u, self.dist_to[u])

    def get_weights(self) -> list:
        mst = []
        n = len(self.edge_to)
        for v in range(1, n):
            mst.append(self.edge_to[v])
        return mst
