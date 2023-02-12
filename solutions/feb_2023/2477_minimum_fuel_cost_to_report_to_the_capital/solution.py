from collections import defaultdict
import math
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj_list = defaultdict(list)

        for a, b in roads:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        fuel_needed = 0

        def dfs(node):
            if node in visited:
                return 0

            nonlocal fuel_needed
            is_leaf = True
            size = 1
            visited.add(node)

            for adj in adj_list[node]:
                if adj in visited:
                    continue

                is_leaf = False
                size += dfs(adj)

            if is_leaf and node != 0:
                fuel_needed += 1
                return 1

            if node != 0:
                fuel_needed += math.ceil(size / seats)

            return size

        dfs(0)

        return fuel_needed
