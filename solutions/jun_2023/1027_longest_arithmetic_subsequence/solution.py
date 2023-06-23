from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}

        for right in range(len(nums)):
            for left in range(right):
                num1, num2 = nums[left], nums[right]
                diff = num1 - num2

                if (right, diff) not in dp:
                    dp[(right, diff)] = 2

                if (left, diff) in dp:
                    dp[(right, diff)] = max(dp[(right, diff)], dp[(left, diff)] + 1)

        return max(dp.values())
