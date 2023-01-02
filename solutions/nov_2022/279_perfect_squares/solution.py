class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        num = 1

        while num**2 <= n:
            squares.append(num**2)
            num += 1

        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(n):
            for sq in squares:
                if sq + i >= n + 1:
                    break

                dp[sq + i] = min(dp[sq + i], dp[i] + 1)

        return dp[-1]
