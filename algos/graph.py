from algos.bag import Bag
from algos.matrix import Matrix


# TODO: CHECK IMPLEMENTATION
class Graph(object):
    _V: int
    _E: int
    _adj: Matrix

    def __init__(self, V: int):
        if V < 0:
            raise Exception('Number of vertices must be non-negative')
        self._V = V
        self._E = 0
        self._adj = Matrix(V, 'int')

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
    # TODO

    def adj(self, v: int):
        self.validate_vertex(v)
        return self._adj.get_object()

    # TODO: IMPLEMENT
    # def degree(self, v: int):
    #     self.validate_vertex(v)
    #     pass

    def render(self):
        print('########## START: GRAPH RENDERING REPRESENTATION #########')
        print('########## | GRAPH:', str(self._V), 'VERTICES,', str(self._E), 'EDGES')

        for v in range(0, self._V):
            print('########## | VERTEX:', str(v))
            for w in self._adj[v].elements:
                print('########## |---- WITH UNDIRECTED EDGE CONNECTING TO VERTEX:', str(w))
            print('##########')
        print('########## END: GRAPH RENDERING REPRESENTATION ######### \n')
