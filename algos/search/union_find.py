class QuickUnion:
    ids: list
    count: int

    def __init__(self, n: int):
        self.count = n
        self.ids = [int] * n

        for i in range(0, n):
            self.ids[i] = i

    def count(self):
        return self.count

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def union(self, p: int, q: int):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root:
            return None

        self.ids[p_root] = q_root
        self.count = self.count - 1

    def find(self, p: int):
        while p != self.ids[p]:
            p = self.ids[p]
        return p


class QuickFind:
    ids: list
    count: int

    def __init__(self, n: int):
        self.count = n
        self.ids = [int] * n

        for i in range(0, n):
            self.ids[i] = i

    def count(self):
        return self.count

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def find(self, p: int):
        return self.ids[p]

    def union(self, p: int, q: int):
        p_id = self.find(p)
        q_id = self.find(q)
        m = len(self.ids)

        if p_id == q_id:
            return None

        for i in range(0, m):
            if self.ids[i] == p_id:
                self.ids[i] = q_id

        self.count = self.count - 1


# TODO: IMPLEMENT WEIGHTED Quick-Union
class WeightedQuickUnion:
    ids: list
    size: list
    count: int

    def __init__(self, n: int):
        self.count = n

        self.ids = [int] * n
        for i in range(0, n):
            self.ids[i] = i

        self.size = [int] * n
        for i in range(0, n):
            self.size[i] = 1

    def count(self):
        return self.count

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def find(self, p: int):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)

        if i == j:
            return None

        if self.size[i] < self.size[j]:
            self.ids[i] = j
            self.size[j] = self.size[j] + self.size[i]
        else:
            self.ids[j] = i
            self.size[i] = self.size[i] + self.size[j]

        self.count = self.count - 1
