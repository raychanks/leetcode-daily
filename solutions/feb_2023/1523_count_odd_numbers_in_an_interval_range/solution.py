import math


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def count(n):
            return math.ceil(n / 2)

        return count(high) - count(low - 1)
