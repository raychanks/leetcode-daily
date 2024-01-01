from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        ptr = 0
        count = 0

        for size in s:
            if ptr >= len(g):
                break

            if size >= g[ptr]:
                count += 1
                ptr += 1

        return count
