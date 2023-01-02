import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ######################################
        # DP with finite state machine, O(n)
        ######################################
        held = -math.inf
        sold = -math.inf
        reset = 0

        for price in prices:
            held = max(held, reset - price)
            reset = max(reset, sold)
            sold = held + price

        return max(int(sold), int(reset))

        ###################
        # Normal DP, O(n^2)
        ###################

        # dp = [0] * len(prices)

        # for i in range(len(dp) - 2, -1, -1):
        #     cost = prices[i]

        #     for j in range(i + 1, len(dp) - 2):
        #         profit = prices[j] - cost
        #         dp[i] = max(dp[i], profit + dp[j + 2])

        #     dp[i] = max(dp[i], dp[i + 1], prices[-1] - cost)

        # return max(dp)
