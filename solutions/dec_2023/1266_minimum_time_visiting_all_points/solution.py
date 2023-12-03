from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cur = points[0]
        time_needed = 0

        for x, y in points[1:]:
            diag = min(abs(x - cur[0]), abs(y - cur[1]))
            horizontal = abs(x - cur[0]) - diag
            vertical = abs(y - cur[1]) - diag

            time_needed += diag + horizontal + vertical
            cur = [x, y]

        return time_needed
