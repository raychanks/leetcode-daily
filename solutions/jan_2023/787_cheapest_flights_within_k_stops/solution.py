from collections import defaultdict, deque
import math
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj_list = defaultdict(list)

        for a, b, cost in flights:
            adj_list[a].append((b, cost))

        visited = defaultdict(lambda: math.inf)
        queue = deque([(src, 0)])
        proximity_count = len(queue)
        min_cost = math.inf
        stops = -1

        while queue and stops <= k:
            node, cur_cost = queue.popleft()

            if node == dst:
                min_cost = min(min_cost, cur_cost)

            for adj, cost_to_adj in adj_list[node]:
                new_cost = cur_cost + cost_to_adj

                if visited[adj] > new_cost:
                    visited[adj] = new_cost
                    queue.append((adj, new_cost))

            proximity_count -= 1

            if proximity_count == 0:
                stops += 1
                proximity_count = len(queue)

        return int(min_cost) if min_cost != math.inf else -1
