import math


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, math.floor(math.sqrt(n)) + 1):
            squares.append(i**2)

        dp = [math.inf] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for sq in squares:
                if i - sq >= 0:
                    dp[i] = min(dp[i], dp[i - sq] + 1)

        return dp[n]
