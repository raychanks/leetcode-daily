from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def LCS(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + LCS(i + 1, j + 1)

            return max(LCS(i + 1, j), LCS(i, j + 1))

        return LCS(0, 0)
