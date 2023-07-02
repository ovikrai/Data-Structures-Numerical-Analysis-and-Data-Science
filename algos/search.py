import math
from algos.graph import Graph
from algos.stack import Stack


# ------------------------- Linear Search ---------------------------- #
# Search in a list
#
# Outputs:
#   Search successful: the index of the target key (i)
#   Search unsuccessful: negative one (-1)
#
# In-Place: requires O(1) of auxiliary memory space.
#
# Runtime T(n):
#   Best: T(n) ~ c
#   Average: T(n) ~ 1/2 * n
#   Worst: T(n) ~ n
#
# Asymptotically Analysis (Big O):
#   Best: T(n) = O(1)
#   Average: T(n) = O(n)
#   Worst: T(n) = O(n)
#
# ----------------------------------------------------------------------- #
# Basic implementations that
# Basic linear search in an unordered list
def linear(a: list, key, low: int, high: int) -> int:
    n = high
    i = low

    while True:
        if a[i] == key:
            return i

        i = i + 1

        if i < n:
            continue
        else:
            return -1


# Sentinel variation of linear search in an unordered list
def linear_sentinel(a: list, key, low: int, high: int) -> int:
    n = high
    i = low

    while True:
        if a[i] == key:
            if i < n:
                return i
            else:
                return -1
        i = i + 1


# Sentinel variation of linear search in an ordered list
# List need to be ordered to this search to work
def linear_ordered(a: list, key) -> int:
    i = 0
    while True:
        if a[i] >= key:
            if a[i] == key:
                return i
            else:
                return -1
        i = i + 1


# ------------------------- Binary Search ---------------------------- #
# Search in a unordered List
#
# Runtime T(n):
#   Best: T(n) ~ c
#   Average: T(n) ~ 1/2 * log(n)
#   Worst: T(n) ~ log(n)
#
# Asymptotically Analysis (Big O):
#   Best: T(n) = O(1)
#   Average: T(n) = O(log(n))
#   Worst: T(n) = O(log(n))
#
# ----------------------------------------------------------------------- #
# Iterative binary search over a list
def binary(a: list, key, left: int, right: int) -> int:
    while left <= right:
        mid = math.floor((left + right) / 2)
        if a[mid] < key:
            left = mid + 1
        elif a[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1


# Alternative binary search over ordered list
# Created by Hermann Bottenbruch, 1962
# List need to be ordered to this search to work
def binary_ordered(a: list, key, left: int, right: int) -> int:
    while left != right:
        mid = math.ceil((left + right) / 2)
        if a[mid] > key:
            right = mid - 1
        else:
            left = mid
    if a[left] == key:
        return left
    return -1


# Leftmost binary search over linear structures
def binary_left(a: list, key, left: int, right: int) -> int:
    while left < right:
        mid = math.floor((left + right) / 2)
        if a[mid] < key:
            left = mid + 1
        else:
            right = mid
    if a[left] == key:
        return left
    return -1


# Rightmost binary search over linear structures
def binary_right(a: list, key, left: int, right: int) -> int:
    while left < right:
        mid = math.floor((left + right) / 2)
        if a[mid] > key:
            right = mid
        else:
            left = mid + 1
    if a[right - 1] == key:
        return right - 1
    return -1


# Recursive binary search over linear structures
def binary_recursive(a: list, key, left: int, right: int) -> int:
    if left <= right:
        mid = math.floor(left + (right - left) / 2)
        if a[mid] == key:
            return mid
        if a[mid] > key:
            return binary_recursive(a, key, left, mid - 1)
        return binary_recursive(a, key, mid + 1, right)
    return -1


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
