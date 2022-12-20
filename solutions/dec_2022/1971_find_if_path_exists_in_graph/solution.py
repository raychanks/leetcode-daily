from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj_list = defaultdict(list)
        seen = set()

        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)

        queue = deque([source])

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for adj in adj_list[node]:
                if adj not in seen:
                    seen.add(node)
                    queue.append(adj)

        return False
