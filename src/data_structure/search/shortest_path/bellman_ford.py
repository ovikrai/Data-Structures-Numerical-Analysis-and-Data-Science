from typing import List
import math

from src.data_structure.graph import WeightedDirectedEdge, WeightedDirectedGraph
from src.data_structure.stack import Stack
from src.data_structure.queue import Queue


# ------------------------- Bellman Ford Algorithm (Queue-based) ---------------------------- #
# Shortest Path Search
# ----------------------------------------------------------------------- #

# FINDING A DIRECTED CYCLE IN A GRAPH
class WeightedDirectedCycle:
    marked: List[bool]
    edge_to: List[int]
    cycle: Stack
    on_stack: List[bool]

    def __init__(self, graph: WeightedDirectedGraph):
        self.on_stack = [bool] * graph.vertices()
        self.edge_to = [int] * graph.vertices()
        self.marked = [bool] * graph.vertices()

        n = len(graph.vertices())
        for i in range(0, n):
            if not self.marked[i]:
                self.dfs(graph, i)

    def dfs(self, graph: WeightedDirectedGraph, v: int):
        self.on_stack[v] = True
        self.marked[v] = True

        for u in graph.adj(v):
            if self.has_cycle():
                return None
            elif not self.marked[u]:
                self.edge_to[u] = v
                self.dfs(graph, u)
            elif self.on_stack[u]:
                self.cycle = Stack()

                i = v
                while i is not u:
                    self.cycle.push(i)
                    i = self.edge_to[i]

                self.cycle.push(u)
                self.cycle.push(v)

        self.on_stack[v] = False

    def has_cycle(self):
        return self.cycle is not None

    def get_cycle(self):
        return self.cycle


class BellmanFordSP:
    edge_to: List[WeightedDirectedEdge]
    dist_to: List[float]
    on_q: List[bool]
    queue: Queue
    cost: int
    cycle: Stack

    def __init__(self, graph: WeightedDirectedGraph, s: int):
        self.dist_to = [float] * graph.vertices()
        self.edge_to = [WeightedDirectedEdge] * graph.vertices()
        self.on_q = [bool] * graph.vertices()
        self.queue = Queue()

        for i in range(0, graph.vertices()):
            self.dist_to[i] = math.inf

        self.dist_to[s] = 0.0
        self.queue.enqueue(s)
        self.on_q[s] = True

        while not self.queue.is_empty() and not self.has_negative_cycle():
            v = self.queue.dequeue()
            self.on_q[v] = False
            self.relax(graph, v)

    def relax(self, graph: WeightedDirectedGraph, v: int):
        e: WeightedDirectedEdge
        for e in graph.adj(v):
            u = e.vertex_to()
            if self.dist_to[u] > self.dist_to[v] + e.get_weight():
                self.dist_to[u] = self.dist_to[v] + e.get_weight()
                self.edge_to[u] = e

                if not self.on_q[u]:
                    self.queue.enqueue(u)
                    self.on_q[u] = True

            self.cost = self.cost + 1
            if self.cost % graph.vertices() == 0:
                self.find_negative_cycle()

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

    def find_negative_cycle(self):
        v: int = len(self.edge_to)
        spt = WeightedDirectedGraph(v)

        for i in range(0, v):
            if self.edge_to[i] is not None:
                spt.add_edge(self.edge_to[i])

        cf = WeightedDirectedCycle(spt)

        self.cycle = cf.get_cycle()

    def has_negative_cycle(self):
        return self.cycle is not None

    def negative_cycle(self):
        return self.cycle
