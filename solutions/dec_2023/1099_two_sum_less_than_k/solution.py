from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        result = -1
        nums.sort()

        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] + num < k:
                    result = max(result, nums[mid] + num)
                    left = mid + 1
                else:
                    right = mid - 1

        return result
