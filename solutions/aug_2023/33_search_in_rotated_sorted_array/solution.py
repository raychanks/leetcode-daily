from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self._find_pivot(nums)

        left_chunk = self._find_target(nums, 0, pivot - 1, target)
        right_chunk = self._find_target(nums, pivot, len(nums) - 1, target)

        return max(left_chunk, right_chunk)

    def _find_target(self, nums, l, r, target):
        left, right = l, r

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if left < len(nums) and nums[left] == target:
            return left
        return -1

    def _find_pivot(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[0] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return left if left < len(nums) else 0
