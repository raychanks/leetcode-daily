from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        @cache
        def solve(i, j):
            if i < 0 and j < 0:
                return 0
            if i < 0:
                return ord(s2[j]) + solve(i, j - 1)
            if j < 0:
                return ord(s1[i]) + solve(i - 1, j)

            if s1[i] == s2[j]:
                return solve(i - 1, j - 1)

            return min(
                ord(s1[i]) + ord(s2[j]) + solve(i - 1, j - 1),
                ord(s1[i]) + solve(i - 1, j),
                ord(s2[j]) + solve(i, j - 1),
            )

        return solve(m - 1, n - 1)
