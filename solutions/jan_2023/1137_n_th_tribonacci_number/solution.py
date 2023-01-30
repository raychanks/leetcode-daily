class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]

        if n <= 2:
            return dp[n]

        for _ in range(3, n + 1):
            tmp = sum(dp)
            dp[0] = dp[1]
            dp[1] = dp[2]
            dp[2] = tmp

        return dp[2]
