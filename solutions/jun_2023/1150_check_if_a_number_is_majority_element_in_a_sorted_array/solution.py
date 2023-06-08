from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]

            if num < target:
                left = mid + 1
            else:
                right = mid - 1

        half = len(nums) // 2

        if left + half >= len(nums):
            return False

        return nums[left + half] == target
