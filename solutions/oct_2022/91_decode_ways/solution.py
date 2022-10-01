class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        dp = [0] * (l + 1)
        if s[l - 1] != "0":
            dp[l - 1] = 1
        dp[l] = 1

        for i in range(l - 2, -1, -1):
            if s[i] != "0":
                dp[i] += dp[i + 1]
            if 10 <= int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]
