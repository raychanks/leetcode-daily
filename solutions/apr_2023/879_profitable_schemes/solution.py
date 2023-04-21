from typing import List


class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        mod = 10**9 + 7
        dp = {}

        def dfs(index, member_involved, profit_so_far):
            if index == len(group):
                return 1 if profit_so_far >= minProfit else 0

            state = (index, member_involved, min(profit_so_far, minProfit))

            if state in dp:
                return dp[state]

            # not take
            count = dfs(index + 1, member_involved, profit_so_far)

            # take
            if member_involved + group[index] <= n:
                count += dfs(
                    index + 1,
                    member_involved + group[index],
                    min(profit_so_far + profit[index], minProfit),
                )

            dp[state] = count % mod

            return dp[state]

        return dfs(0, 0, 0)
