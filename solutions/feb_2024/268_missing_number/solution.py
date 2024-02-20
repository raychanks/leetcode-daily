from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i in range(len(nums) + 1):
            missing ^= i
            if i < len(nums):
                missing ^= nums[i]
        return missing
