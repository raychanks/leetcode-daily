from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        adj_list = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            adj_list[a].append((b, succProb[i]))
            adj_list[b].append((a, succProb[i]))

        visited = set()
        max_heap = [(-1, start)]
        max_prob = [-1] * n
        max_prob[start] = 1

        while max_heap:
            p1, node = heapq.heappop(max_heap)
            p1 *= -1

            if node == end:
                return p1

            for adj, p2 in adj_list[node]:
                if adj in visited:
                    continue

                if p1 * p2 > max_prob[adj]:
                    max_prob[adj] = p1 * p2
                    heapq.heappush(max_heap, (-p1 * p2, adj))

            visited.add(node)

        return 0
