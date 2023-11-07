import heapq
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrive_at = [d / s for d, s in zip(dist, speed)]
        heapq.heapify(arrive_at)
        elimination_count = 0
        time_elapsed = 0

        while arrive_at and time_elapsed < arrive_at[0]:
            heapq.heappop(arrive_at)
            elimination_count += 1
            time_elapsed += 1

        return elimination_count
