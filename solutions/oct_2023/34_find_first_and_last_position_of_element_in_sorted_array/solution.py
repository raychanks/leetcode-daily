import random
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.search(nums, target)
        end = self.search(nums, target + 1)

        if start == end:
            return [-1, -1]
        return [start, end - 1]

    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
