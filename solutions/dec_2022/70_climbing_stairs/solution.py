class Solution:
    def climbStairs(self, n: int) -> int:
        dp1, dp2 = 1, 1

        for _ in range(2, n + 1):
            tmp = dp1 + dp2
            dp1 = dp2
            dp2 = tmp

        return dp2
