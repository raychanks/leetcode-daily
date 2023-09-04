class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            next_dp = [0] * n
            next_dp[0] = 1

            for c in range(1, n):
                next_dp[c] = dp[c] + next_dp[c - 1]

            dp = next_dp

        return dp[-1]
