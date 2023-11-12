from collections import defaultdict, deque
import math
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        distances = defaultdict(lambda: math.inf)
        distances[source] = 0

        visited = set()
        visited_rs = set()
        routes_set = [set(r) for r in routes]
        queue = deque([source])

        while queue:
            cur = queue.popleft()

            if cur in visited:
                continue

            visited.add(cur)

            for i, rs in enumerate(routes_set):
                if cur in rs and i not in visited_rs:
                    visited_rs.add(i)
                    for bus_stop in rs:
                        queue.append(bus_stop)
                        distances[bus_stop] = min(
                            distances[bus_stop], 1 + distances[cur]
                        )

        return distances[target] if distances[target] != math.inf else -1
