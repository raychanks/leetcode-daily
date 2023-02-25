from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low = prices[0]

        for price in prices:
            if price < low:
                low = price
            else:
                max_profit = max(max_profit, price - low)

        return max_profit
