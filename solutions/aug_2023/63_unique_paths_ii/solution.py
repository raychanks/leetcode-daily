from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * (n + 1)
        for i, val in enumerate(obstacleGrid[0], 1):
            if val == 1:
                break
            dp[i] = 1

        for r in range(1, m):
            next_dp = [0] * (n + 1)

            for c in range(n):
                if obstacleGrid[r][c]:
                    continue

                next_dp[c + 1] = dp[c + 1] + next_dp[c]

            dp = next_dp

        return dp[-1]
