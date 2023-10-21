from collections import Counter
import heapq
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        max_heap = [0]
        gone_nums = Counter()

        for i in range(len(nums)):
            while gone_nums[-max_heap[0]] != 0:
                gone_nums[-max_heap[0]] -= 1
                heapq.heappop(max_heap)

            prev_max = -max_heap[0]
            dp[i] = nums[i] + prev_max
            heapq.heappush(max_heap, -dp[i])

            if i - k >= 0:
                gone_nums[dp[i - k]] += 1

        return max(dp)
