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

class LazyPrimMST:
    marked: list
    mst: Queue
    pq: PriorityQueue

    def __int__(self, graph):
        self.pq = PriorityQueue(1)


