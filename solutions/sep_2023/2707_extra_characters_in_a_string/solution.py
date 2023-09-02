from functools import cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)

        @cache
        def dfs(i):
            if i == len(s):
                return 0

            min_count = len(s)

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in word_set:
                    min_count = min(min_count, dfs(j))

            min_count = min(min_count, 1 + dfs(i + 1))

            return min_count

        return dfs(0)
