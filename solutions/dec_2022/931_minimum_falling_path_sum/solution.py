from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n

        for i in range(m - 1, -1, -1):
            next_dp = [0] * n

            for j in range(n):
                val = matrix[i][j]
                left_idx = max(0, j - 1)
                right_idx = min(n - 1, j + 1)

                next_dp[j] = val + min(dp[left_idx : right_idx + 1])

            dp = next_dp

        return min(dp)
