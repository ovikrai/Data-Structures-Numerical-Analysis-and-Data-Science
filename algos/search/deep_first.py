from algos.graph import Graph
from algos.stack import Stack


# ------------------------- Depth First Search ---------------------------- #
# Search in a graph
#
# Runtime T(n):
#   Best: T(n) ~ c
#   Average: T(n) ~ 1/2 * (|V| + |E|)
#   Worst: T(n) ~ |V| + |E|
#
# Asymptotically Analysis (Big O):
#   Best: T(n) = O(1)
#   Average: T(n) = )(|V| + |E|)
#   Worst: T(n) = O(|V| + |E|)
#
# ----------------------------------------------------------------------- #
class DepthFirstSearch(object):
    marked: list
    edge_to: list
    source_vertex: int

    def __init__(self, G: Graph, source_vertex: int):
        self.source_vertex = source_vertex
        self.edge_to = [0] * G.vertex_count()
        self.marked = [False] * G.vertex_count()
        G.validate_vertex(source_vertex)
        self._dfs(G, source_vertex)

    def _dfs(self, G: Graph, v: int):
        self.marked[v] = True
        for w in G.adj(v).elements:
            if not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(G, w)

    def has_path_to(self, G: Graph, v: int) -> bool:
        G.validate_vertex(v)
        return self.marked[v]

    def path_to(self, G: Graph, v: int) -> Stack:
        G.validate_vertex(v)
        if not self.has_path_to(G, v):
            return None

        path = Stack()
        x = v
        while x is not self.source_vertex:
            path.push(x)
            x = self.edge_to[x]

        path.push(self.source_vertex)
        return path
