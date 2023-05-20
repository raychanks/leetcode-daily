from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj_list = defaultdict(list)

        for eq, val in zip(equations, values):
            a, b = eq
            adj_list[a].append((b, val))
            adj_list[b].append((a, 1 / val))

        visited = set()

        def dfs(src, dst, total_cost):
            if src not in adj_list or dst not in adj_list:
                return -1.0

            if src == dst:
                return total_cost

            visited.add(src)

            for adj, cost in adj_list[src]:
                if adj in visited:
                    continue

                val = dfs(adj, dst, total_cost * cost)

                if val != -1.0:
                    visited.remove(src)
                    return val

            visited.remove(src)
            return -1.0

        return [dfs(v1, v2, 1.0) for v1, v2 in queries]
