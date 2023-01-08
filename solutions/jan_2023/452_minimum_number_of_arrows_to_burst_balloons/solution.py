from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        cur_pos = points[0][0] - 1
        count = 0

        for point in points:
            start, end = point

            if cur_pos >= start:
                cur_pos = min(cur_pos, end)
                continue

            count += 1
            cur_pos = end

        return count
