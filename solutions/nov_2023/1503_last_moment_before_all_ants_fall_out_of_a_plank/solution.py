from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_heading_left = max(left or [0])
        min_heading_right = min(right or [n])

        return max(n - min_heading_right, max_heading_left)
