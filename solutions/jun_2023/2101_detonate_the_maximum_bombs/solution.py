from collections import defaultdict, deque
import math
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if not bombs:
            return 0

        graph = defaultdict(list)

        for i, bomb in enumerate(bombs):
            x1, y1, r1 = bomb

            for j in range(len(bombs)):
                if i == j:
                    continue

                x2, y2, _ = bombs[j]

                if math.hypot(x1 - x2, y1 - y2) <= r1:
                    graph[i].append(j)

        max_detonated = 0

        for i in range(len(bombs)):
            visited = set()
            queue = deque([i])
            detonated = 0

            while queue:
                bomb_idx = queue.popleft()

                if bomb_idx in visited:
                    continue

                visited.add(bomb_idx)
                detonated += 1
                queue.extend(graph[bomb_idx])

            max_detonated = max(max_detonated, detonated)

        return max_detonated
