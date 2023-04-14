from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def solve(start, end):
            if start == end:
                return 0

            if start == end - 1:
                return 1

            first, last = s[start], s[end - 1]

            if first == last:
                return 2 + solve(start + 1, end - 1)

            return max(
                solve(start + 1, end),
                solve(start, end - 1),
            )

        return solve(0, len(s))
