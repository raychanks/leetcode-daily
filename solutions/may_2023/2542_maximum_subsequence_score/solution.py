import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        max_score = 0
        current_sum = 0

        min_heap = []
        for i in range(k):
            val = nums[i][0]
            current_sum += val
            heapq.heappush(min_heap, val)

        max_score = max(max_score, current_sum * nums[k - 1][1])

        for i in range(k, len(nums)):
            val = nums[i][0]
            smallest_in_heap = heapq.heappop(min_heap)
            score = (current_sum + val - smallest_in_heap) * nums[i][1]

            if score > max_score:
                max_score = score

            current_sum = current_sum + val - smallest_in_heap
            heapq.heappush(min_heap, val)

        return max_score
