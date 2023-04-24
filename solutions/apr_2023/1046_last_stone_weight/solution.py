import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            a, b = -heapq.heappop(max_heap), -heapq.heappop(max_heap)

            if a == b:
                continue

            heapq.heappush(max_heap, -(a - b))

        return 0 if not max_heap else -heapq.heappop(max_heap)
