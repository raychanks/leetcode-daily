import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0

        for _ in range(len(sticks) - 1):
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            merged = a + b
            cost += merged
            heapq.heappush(sticks, merged)

        return cost
