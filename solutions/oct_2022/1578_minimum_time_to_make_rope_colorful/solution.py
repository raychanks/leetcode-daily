from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, r = 0, 0
        cur_max = 0
        cost = 0

        while r < len(colors):
            t = neededTime[r]

            if colors[l] == colors[r]:
                r += 1
                cur_max = max(cur_max, t)
                cost += t
            else:
                l = r
                cost -= cur_max
                cur_max = 0

        return cost - cur_max
