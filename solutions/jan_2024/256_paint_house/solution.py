from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0, 0, 0]

        for cost in costs:
            min_red = cost[0] + min(dp[1], dp[2])
            min_blue = cost[1] + min(dp[0], dp[2])
            min_green = cost[2] + min(dp[0], dp[1])
            dp = [min_red, min_blue, min_green]

        return min(dp)
