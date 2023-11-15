from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        cur = 1

        for num in arr:
            if num >= cur:
                cur += 1

        return cur - 1
