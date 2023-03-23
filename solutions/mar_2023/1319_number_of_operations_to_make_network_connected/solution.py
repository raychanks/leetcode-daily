from collections import defaultdict, deque
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        adj_list = defaultdict(list)

        for a, b in connections:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        queue = deque()
        disjoint_set_count = 0

        for i in range(n):
            if i not in visited:
                queue.append(i)
                disjoint_set_count += 1

            while queue:
                node = queue.popleft()

                if node in visited:
                    continue

                visited.add(node)

                for adj in adj_list[node]:
                    if adj not in visited:
                        queue.append(adj)

        return disjoint_set_count - 1
