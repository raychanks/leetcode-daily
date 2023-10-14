from functools import cache
import math
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [math.inf] * (n + 1)
        dp[0] = 0

        for i in range(n - 1, -1, -1):
            next_dp = [math.inf] * (n + 1)
            next_dp[0] = 0

            for j in range(1, n + 1):
                paint = cost[i] + dp[max(0, j - 1 - time[i])]
                dont_paint = dp[j]
                next_dp[j] = min(paint, dont_paint)

            dp = next_dp

        return dp[-1]


class SolutionTopDown:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @cache
        def solve(i, walls_left):
            if walls_left <= 0:
                return 0

            if i == n:
                return math.inf

            return min(
                cost[i] + solve(i + 1, walls_left - 1 - time[i]),
                solve(i + 1, walls_left),
            )

        return solve(0, n)
