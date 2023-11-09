from typing import List


class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        def calc_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        distances = 0
        min_distance = height * width * 2 * len(nuts)

        for nut in nuts:
            distances += calc_distance(tree, nut)

        for nut in nuts:
            min_distance = min(
                min_distance,
                distances * 2 - calc_distance(tree, nut) + calc_distance(squirrel, nut),
            )

        return min_distance
