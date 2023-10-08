from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_max, nums1_min = max(nums1), min(nums1)
        nums2_max, nums2_min = max(nums2), min(nums2)

        if nums1_max < 0 and nums2_min > 0:
            return nums1_max * nums2_min
        if nums2_max < 0 and nums1_min > 0:
            return nums2_max * nums1_min

        @cache
        def solve(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            return max(
                nums1[i] * nums2[j] + solve(i + 1, j + 1),
                solve(i, j + 1),
                solve(i + 1, j),
            )

        return solve(0, 0)
