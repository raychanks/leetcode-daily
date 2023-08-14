import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif min_heap[0] < num:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]
