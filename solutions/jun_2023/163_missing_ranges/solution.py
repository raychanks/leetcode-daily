from typing import List


class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int
    ) -> List[List[int]]:
        missing_ranges = []
        start = lower

        for num in nums:
            if num > start:
                missing_ranges.append([start, num - 1])
            start = num + 1

        if start <= upper:
            missing_ranges.append([start, upper])

        return missing_ranges
