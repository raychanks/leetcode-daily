import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 10**9

        while left < right:
            mid = left + (right - left) // 2
            hour_left = h

            for pile in piles:
                hour_left -= math.ceil(pile / mid)

            if hour_left < 0:
                left = mid + 1
            else:
                right = mid

        return left
