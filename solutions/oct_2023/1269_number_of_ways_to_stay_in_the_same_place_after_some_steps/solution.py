from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        n = min(arrLen, steps)
        dp = [0] * n
        dp[0] = 1

        for _ in range(steps):
            next_dp = [0] * n

            for j in range(n):
                if j > 0:
                    next_dp[j] += dp[j - 1]
                if j < n - 1:
                    next_dp[j] += dp[j + 1]
                next_dp[j] += dp[j]
                next_dp[j] %= MOD

            dp = next_dp

        return dp[0]


class SolutionTopDown:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        @cache
        def solve(i, steps_left):
            if steps_left == 0:
                return 1 if i == 0 else 0

            go_left, stay, go_right = 0, 0, 0
            if i > 0:
                go_left = solve(i - 1, steps_left - 1)
            if i < arrLen - 1:
                go_right = solve(i + 1, steps_left - 1)
            stay = solve(i, steps_left - 1)

            return (go_left + stay + go_right) % MOD

        return solve(0, steps)
