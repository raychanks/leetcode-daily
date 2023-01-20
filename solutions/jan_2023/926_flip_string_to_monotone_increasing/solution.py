class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = 0
        num_ones = 0

        for i in range(len(s)):
            if s[i] == "1":
                num_ones += 1
            else:
                dp = min(dp + 1, num_ones)

        return dp
