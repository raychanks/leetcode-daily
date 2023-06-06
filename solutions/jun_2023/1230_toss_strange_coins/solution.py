from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [0.0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            next_dp = [0.0] * (n + 1)

            for j in range(n + 1):
                if j == 0:
                    next_dp[j] = dp[j] * (1 - prob[i])
                else:
                    next_dp[j] = dp[j] * (1 - prob[i]) + dp[j - 1] * prob[i]

            dp = next_dp

        return dp[target]
