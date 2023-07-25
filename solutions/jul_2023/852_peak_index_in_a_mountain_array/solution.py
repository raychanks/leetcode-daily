from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            mid_val = arr[mid]
            mid_left_val = -(10**9) if mid == 0 else arr[mid - 1]
            mid_right_val = -(10**9) if mid == len(arr) - 1 else arr[mid + 1]

            if mid_left_val < mid_val and mid_right_val < mid_val:
                return mid

            if mid_left_val > mid_val:
                right = mid - 1
            elif mid_right_val > mid_val:
                left = mid + 1

        return left
