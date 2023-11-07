from utils import swim, sink, swap


# Binary Heap Priority Queue
class PriorityQueue:
    # priority queue
    pq: list
    n: int

    def __init__(self, max_n):
        max_n = max_n + 1
        self.pq = [None] * max_n
        self.n = 0

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n

    def insert(self, value):
        self.n = self.n + 1
        self.pq[self.n] = value
        swim(self.pq, self.n)

    def delete_max(self):
        max_top = self.pq[1]
        self.n = self.n - 1
        swap(self.pq, 1, self.n)
        self.pq[self.n + 1] = None
        sink(self.pq, 1)
        return max_top
