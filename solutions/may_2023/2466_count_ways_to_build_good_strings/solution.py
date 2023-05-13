class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            ways = 0

            if i - zero >= 0:
                ways += dp[i - zero]
            if i - one >= 0:
                ways += dp[i - one]

            dp[i] = ways % mod

        return sum(dp[low : high + 1]) % mod
