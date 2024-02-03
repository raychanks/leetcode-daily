from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)

        for i in range(len(arr) - 1, -1, -1):
            for j in range(1, k + 1):
                if i + j > len(arr):
                    break

                local_sum = max(arr[i : i + j]) * j
                dp[i] = max(dp[i], local_sum + dp[i + j])

        return dp[0]
