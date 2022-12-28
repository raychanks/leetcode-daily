import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        stones_remaining = sum(piles)
        max_heap = [-x for x in piles]
        heapq.heapify(max_heap)

        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            remove = largest // 2
            stones_remaining -= remove
            heapq.heappush(max_heap, -(largest - remove))

        return stones_remaining
