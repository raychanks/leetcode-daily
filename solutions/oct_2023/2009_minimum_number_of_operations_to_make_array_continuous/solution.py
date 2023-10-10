from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        deduplicated = set(nums)
        sorted_nums = list(sorted(deduplicated))
        min_operations = n

        for i in range(len(sorted_nums)):
            left, right = i, len(sorted_nums) - 1
            end = sorted_nums[left] + n - 1

            while left <= right:
                mid = (left + right) // 2
                if sorted_nums[mid] <= end:
                    left = mid + 1
                else:
                    right = mid - 1

            included = left - i
            min_operations = min(min_operations, n - included)

        return min_operations
