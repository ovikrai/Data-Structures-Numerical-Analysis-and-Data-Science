from src.data_structure.queue import Queue
from src.data_structure.search.union_find import QuickUnion
from src.data_structure.priority_queue import PriorityQueue
from src.data_structure.graph import WeightedGraph, WeightedEdge


# ------------------------- Kruskal Minimum Spanning Tree ---------------------------- #
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

class KruskalMST:
    mst: Queue

    def __init__(self, graph: WeightedGraph):
        pq = PriorityQueue(graph.edges())
        uf = QuickUnion(graph.edges())

        while not pq.is_empty() and self.mst.size() < graph.vertices() - 1:
            e: WeightedEdge = pq.delete(0)
            v = e.either()
            u = e.other(v)
            uf.union(v, u)
            self.mst.enqueue(e)

    def get_edges(self):
        return self.mst
