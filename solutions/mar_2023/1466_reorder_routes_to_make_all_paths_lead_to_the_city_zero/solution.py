from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        adj_list = defaultdict(list)
        adj_list_towards = defaultdict(list)

        for a, b in connections:
            adj_list[a].append(b)
            adj_list_towards[b].append(a)

        queue = deque([0])
        seen = set()

        while queue:
            node = queue.popleft()
            seen.add(node)

            for adj in adj_list[node]:
                if adj in seen:
                    continue

                count += 1
                queue.append(adj)

            for adj in adj_list_towards[node]:
                if adj in seen:
                    continue

                queue.append(adj)

        return count
