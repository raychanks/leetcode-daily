from collections import defaultdict
import heapq
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)

        for idx, p in enumerate(parent):
            if p == -1:
                continue

            tree[p].append(idx)

        longest_len = 1

        def dfs(node):
            if not tree[node]:
                return 1

            different_char_lens = []
            char = s[node]

            for child in tree[node]:
                sub_path_len = dfs(child)

                if char != s[child]:
                    different_char_lens.append(sub_path_len)

            different_char_lens.sort(reverse=True)

            two_chain = sum(different_char_lens[:2]) + 1

            nonlocal longest_len
            longest_len = max(longest_len, two_chain)

            return max(sum(different_char_lens[:1]) + 1, 1)

        dfs(0)

        return longest_len
