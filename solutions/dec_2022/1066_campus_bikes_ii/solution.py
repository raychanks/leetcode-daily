from functools import cache
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def get_distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        @cache
        def dfs(worker_idx, bit_mask):
            if worker_idx == len(workers):
                return 0

            min_distance = 10**9

            for bike_idx, bike in enumerate(bikes):
                bit = 1 << bike_idx

                if bit_mask & bit:
                    continue

                distance = get_distance(workers[worker_idx], bike)
                distance += dfs(worker_idx + 1, bit_mask ^ bit)
                min_distance = min(min_distance, distance)

            return min_distance

        return dfs(0, 0)
