from collections import defaultdict, deque
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for a, b in dislikes:
            adj_list[a].append(b)
            adj_list[b].append(a)

        colors = [-1] * n
        queue: deque[tuple[int, int]] = deque([(1, 0)])
        processed_num = 1

        while queue or processed_num < n:
            if not queue:
                for i in range(processed_num - 1, n):
                    if colors[i] == -1:
                        queue.append((i + 1, 0))
                        processed_num = i + 1
                        break
                else:
                    break
                continue

            node, color = queue.popleft()

            if colors[node - 1] not in {-1, color}:
                return False

            colors[node - 1] = color

            for adj in adj_list[node]:
                if colors[adj - 1] == -1:
                    queue.append((adj, 1 - color))

        return True
