from collections import defaultdict
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[a].append(b)

        in_degree = defaultdict(int)
        for i in range(n):
            if i not in in_degree:
                in_degree[i] = 0

            for destination in adj_list[i]:
                in_degree[destination] += 1

        return [node for node, degree in in_degree.items() if degree == 0]
