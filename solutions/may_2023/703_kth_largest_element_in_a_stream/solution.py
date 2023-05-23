import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self._min_heap = []
        self._k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self._min_heap) < self._k:
            heapq.heappush(self._min_heap, val)
        else:
            if val > self._min_heap[0]:
                heapq.heapreplace(self._min_heap, val)

        return self._min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
