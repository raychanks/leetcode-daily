from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        days_set = set(days)

        def solve(cur_day):
            if cur_day < 0:
                return 0

            if dp[cur_day] == 0:
                if cur_day in days_set:
                    dp[cur_day] = min(
                        solve(cur_day - 1) + costs[0],
                        solve(cur_day - 7) + costs[1],
                        solve(cur_day - 30) + costs[2],
                    )
                else:
                    dp[cur_day] = solve(cur_day - 1)

            return dp[cur_day]

        return solve(365)
