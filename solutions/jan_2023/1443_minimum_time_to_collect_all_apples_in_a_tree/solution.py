from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_list = defaultdict(list)
        distances = [0] * n

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        seen = set()

        def solve(node) -> bool:
            if node in seen:
                return False

            seen.add(node)
            t = 0

            for child in adj_list[node]:
                if solve(child):
                    t += distances[child] + 1

            if t != 0:
                hasApple[node] = True

            distances[node] = t

            return t != 0 or hasApple[node]

        solve(0)

        return distances[0] * 2
