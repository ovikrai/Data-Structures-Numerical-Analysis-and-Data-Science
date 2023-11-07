from algos.graph import UndirectedGraph
from algos.queue import Queue
from algos.stack import Stack


# ------------------------- Breadth First Search ---------------------------- #
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

class BreadthFirstPaths:
    marked: list
    edge_to: list
    source_vertex: int

    def __int__(self, graph: UndirectedGraph, source_vertex: int):
        self.marked = [bool] * graph.vertices()
        self.edge_to = [int] * graph.vertices()
        self.source_vertex = source_vertex
        self.bfs(graph, source_vertex)

    def bfs(self, graph: UndirectedGraph, source_vertex: int):
        queue = Queue()
        self.marked[source_vertex] = True
        queue.enqueue(source_vertex)

        while not queue.is_empty():
            v = queue.dequeue()
            for w in graph.adj(v):
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    queue.enqueue(w)

    def has_path_to(self, v: int) -> bool:
        return self.marked[v]

    def path_to(self, v: int):
        if not self.has_path_to(v):
            return None

        path = Stack()

        x = v
        while x != self.source_vertex:
            path.push(x)
            x = self.edge_to[x]
        path.push(self.source_vertex)

        return path
