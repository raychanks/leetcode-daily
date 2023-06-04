from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0

        for i in range(len(isConnected)):
            if i in visited:
                continue

            count += 1
            queue = deque([i])

            while queue:
                node_idx = queue.popleft()

                if node_idx in visited:
                    continue

                visited.add(node_idx)

                for j, v in enumerate(isConnected[node_idx]):
                    if v == 1:
                        queue.append(j)

        return count
