from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        peak = nums[0]
        deficit = 0

        for i, num in enumerate(nums):
            if num == peak:
                continue

            if num < peak:
                deficit += peak - num
                continue

            if num - peak <= deficit:
                deficit -= num - peak
                continue

            div, mod = divmod(peak * i - deficit + num, i + 1)

            if mod == 0:
                peak = div
                deficit = 0
            else:
                peak = div + 1
                deficit = i + 1 - mod

        return peak
