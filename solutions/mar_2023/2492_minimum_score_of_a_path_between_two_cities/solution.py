from collections import defaultdict, deque
import math
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for road in roads:
            a, b, distance = road
            adj_list[a].append((b, distance))
            adj_list[b].append((a, distance))

        seen = set()
        queue = deque([1])
        min_distance = math.inf

        while queue:
            node = queue.popleft()
            if node in seen:
                continue

            seen.add(node)

            for adj, dist in adj_list[node]:
                if dist < min_distance:
                    min_distance = dist

                if adj not in seen:
                    queue.append(adj)

        return int(min_distance)
