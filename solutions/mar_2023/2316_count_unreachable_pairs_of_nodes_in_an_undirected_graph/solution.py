from collections import defaultdict, deque
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj_list = self._build_adj_list(edges)
        group_sizes = self._get_group_sizes(n, adj_list)
        size_sum = sum(group_sizes)
        answer = 0

        for size in group_sizes:
            answer += size * (size_sum - size)

        return answer // 2

    def _build_adj_list(self, edges):
        adj_list = defaultdict(list)

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        return adj_list

    def _get_group_sizes(self, n, adj_list):
        visited = set()
        queue = deque()
        group_sizes = []

        for i in range(n):
            queue.append(i)
            size = 0

            while queue:
                node = queue.popleft()

                if node in visited:
                    continue

                visited.add(node)
                size += 1

                for adj in adj_list[node]:
                    if adj not in visited:
                        queue.append(adj)

            if size > 0:
                group_sizes.append(size)

        return group_sizes
