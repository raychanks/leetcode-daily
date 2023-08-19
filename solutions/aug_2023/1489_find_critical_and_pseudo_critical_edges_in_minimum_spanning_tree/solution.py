from typing import List


class UnionFind:
    def __init__(self, n) -> None:
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False

        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
            self.ranks[p1] += self.ranks[p2]
        else:
            self.parents[p1] = p2
            self.ranks[p2] += self.ranks[p1]

        return True

    def find(self, v):
        while v != self.parents[v]:
            self.parents[v] = self.parents[self.parents[v]]
            v = self.parents[v]
        return v


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        mst_weight = 0
        uf = UnionFind(n)
        for u, v, w, i in edges:
            if uf.union(u, v):
                mst_weight += w

        critical, pseudo = [], []
        for u1, v1, w1, i in edges:
            weight = 0
            uf = UnionFind(n)
            for u2, v2, w2, j in edges:
                if i != j and uf.union(u2, v2):
                    weight += w2
            if weight > mst_weight or max(uf.ranks) != n:
                critical.append(i)
                continue

            weight = w1
            uf = UnionFind(n)
            uf.union(u1, v1)
            for u2, v2, w2, j in edges:
                if uf.union(u2, v2):
                    weight += w2
            if weight == mst_weight:
                pseudo.append(i)

        return [critical, pseudo]
