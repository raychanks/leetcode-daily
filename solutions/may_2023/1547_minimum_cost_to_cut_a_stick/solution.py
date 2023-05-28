from functools import cache
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dfs(start, end):
            length = end - start
            cost = 10**9

            for cut in cuts:
                if start < cut < end:
                    cost = min(cost, length + dfs(start, cut) + dfs(cut, end))

            return cost if cost != 10**9 else 0

        return dfs(0, n)
