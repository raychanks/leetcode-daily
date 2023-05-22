from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        min_heap = []

        for num, freq in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                if min_heap[0][0] < freq:
                    heapq.heapreplace(min_heap, (freq, num))

        result = []

        for _ in range(len(min_heap)):
            _, num = heapq.heappop(min_heap)
            result.append(num)

        return result
