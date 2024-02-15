from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        cur_sum = 0
        prefix_sum = []
        for num in nums:
            cur_sum += num
            prefix_sum.append(cur_sum)

        for i in range(len(nums) - 1, 1, -1):
            if prefix_sum[i] < prefix_sum[i - 1] * 2:
                return prefix_sum[i]

        return -1
