from algos.bag import Bag


class Graph(object):
    _V: int
    _E: int
    _adj: list

    def __init__(self, V: int):
        if V < 0:
            raise Exception('Number of vertices must be non-negative')
        self._V = V
        self._E = 0
        self._adj = [None] * V

        for v in range(0, V):
            self._adj[v] = Bag()

    def vertex_count(self) -> int:
        return self._V

    def edge_count(self) -> int:
        return self._E

    def validate_vertex(self, v: int):
        if v < 0 or v >= self._V:
            raise Exception("vertex " + str(v) + " is not between 0 and " + str(self._V - 1))

    def add_edge(self, v: int, w: int):
        self.validate_vertex(v)
        self.validate_vertex(w)
        self._E = self._E + 1
        self._adj[v].add(w)
        self._adj[w].add(v)

    def adj(self, v: int):
        self.validate_vertex(v)
        return self._adj[v]

    def degree(self, v: int):
        self.validate_vertex(v)
        return self._adj[v].size()

    def render(self):
        print('########## START: GRAPH RENDERING REPRESENTATION #########')
        print('########## | GRAPH:', str(self._V), 'VERTICES,', str(self._E), 'EDGES')

        for v in range(0, self._V):
            print('########## | VERTEX:', str(v))
            for w in self._adj[v].elements:
                print('########## |---- WITH UNDIRECTED EDGE CONNECTING TO VERTEX:', str(w))
            print('##########')
        print('########## END: GRAPH RENDERING REPRESENTATION ######### \n')
