from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) // 2

        while left < right:
            mid = left + (right - left) // 2
            idx = mid * 2

            if idx == len(nums):
                return nums[-1]

            if nums[idx + 1] == nums[idx]:
                left = mid + 1
            else:
                right = mid

        return nums[left * 2]
