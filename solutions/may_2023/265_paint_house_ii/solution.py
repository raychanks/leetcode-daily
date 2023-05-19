from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        MAX = 10**9
        k = len(costs[0])
        dp = [0] * k

        for cost in costs:
            next_dp = [0] * k
            min_1, min_2 = MAX, MAX
            for c in dp:
                if c <= min_1:
                    min_2 = min_1
                    min_1 = c
                elif c <= min_2:
                    min_2 = c

            for i, c in enumerate(cost):
                if dp[i] == min_1:
                    next_dp[i] = c + min_2
                else:
                    next_dp[i] = c + min_1

            dp = next_dp

        return min(dp)
