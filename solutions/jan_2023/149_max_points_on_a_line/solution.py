from collections import Counter
import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        def get_slope(p1, p2):
            if p1[0] == p2[0]:
                return math.inf

            return (p1[1] - p2[1]) / (p1[0] - p2[0])

        max_points = 2

        for i in range(len(points)):
            counter = Counter()

            for j in range(len(points)):
                if i == j:
                    continue

                slope = get_slope(points[i], points[j])
                counter[slope] += 1

            max_points = max(max_points, max(counter.values()) + 1)

        return max_points
