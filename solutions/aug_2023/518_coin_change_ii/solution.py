from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(amount_left, coin_idx):
            if amount_left == 0:
                return 1

            if coin_idx == len(coins):
                return 0

            if coins[coin_idx] > amount_left:
                return dfs(amount_left, coin_idx + 1)

            return dfs(amount_left - coins[coin_idx], coin_idx) + dfs(
                amount_left, coin_idx + 1
            )

        return dfs(amount, 0)
