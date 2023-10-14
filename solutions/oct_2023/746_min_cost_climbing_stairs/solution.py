from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # --- bottom up ---
        dp = [cost[-2], cost[-1]]

        for i in range(len(cost) - 3, -1, -1):
            min_cost = cost[i] + min(dp)
            dp = [min_cost, dp[0]]

        return min(dp)

        # --- top down ---
        # @cache
        # def solve(i):
        #     if i >= len(cost):
        #         return 0

        #     return cost[i] + min(solve(i + 1), solve(i + 2))

        # return min(solve(0), solve(1))
