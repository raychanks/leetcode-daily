import math
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix_avg = [0]
        cur_sum = 0

        for num in nums:
            cur_sum += num
            prefix_avg.append(cur_sum // len(prefix_avg))

        suffix_avg = [0]
        cur_sum = 0

        for num in nums[::-1]:
            cur_sum += num
            suffix_avg.append(cur_sum // len(suffix_avg))

        min_avg_diff = math.inf
        min_idx = len(nums)

        for i in range(len(nums)):
            avg = abs(prefix_avg[i + 1] - suffix_avg[len(nums) - i - 1])

            if avg < min_avg_diff:
                min_avg_diff = avg
                min_idx = i

        return min_idx
