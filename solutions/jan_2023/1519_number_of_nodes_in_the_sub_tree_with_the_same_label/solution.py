from collections import Counter, defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        result = [1] * n
        seen = set()
        counters = [Counter() for _ in range(n)]

        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            char = labels[node]
            counters[node][char] += 1

            for child in adj_list[node]:
                if child not in seen:
                    dfs(child)

                    for k, v in counters[child].items():
                        counters[node][k] += v

        dfs(0)

        for i, char in enumerate(labels):
            result[i] = counters[i][char]

        return result
