class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0] * target
        for i in range(min(k, len(dp))):
            dp[i] = 1

        for i in range(2, n + 1):
            new_dp = [0] * target
            for j in range(len(new_dp)):
                for val in range(1, k + 1):
                    if 0 <= j - val < len(dp):
                        new_dp[j] += dp[j - val]

            dp = new_dp

        return dp[len(dp) - 1] % (10**9 + 7)
