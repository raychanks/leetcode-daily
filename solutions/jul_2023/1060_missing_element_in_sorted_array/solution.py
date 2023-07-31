from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        unique_count = nums[-1] - nums[0] + 1

        if k > unique_count - n:
            return nums[-1] + (k - (unique_count - n))

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            unique_count = nums[mid] - nums[0] + 1
            missing_count = unique_count - (mid + 1)

            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1

        return nums[0] + left - 1 + k
