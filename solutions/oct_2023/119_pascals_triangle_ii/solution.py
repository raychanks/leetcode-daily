from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [0] * (rowIndex + 1)
        dp[0] = 1

        for i in range(rowIndex + 1):
            next_dp = [0] * (rowIndex + 1)
            next_dp[0] = 1

            for j in range(1, i + 1):
                next_dp[j] = dp[j - 1] + dp[j]

            dp = next_dp

        return dp
