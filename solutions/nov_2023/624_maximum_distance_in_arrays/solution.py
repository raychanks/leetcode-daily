from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        top_two = []

        for i, arr in enumerate(arrays):
            top_two.append((arr[-1], i))

            if len(top_two) > 2:
                top_two.sort(reverse=True)
                top_two.pop()

        max_dist = 0

        for i, arr in enumerate(arrays):
            if i != top_two[0][1]:
                max_dist = max(max_dist, abs(top_two[0][0] - arr[0]))
            else:
                max_dist = max(max_dist, abs(top_two[1][0] - arr[0]))

        return max_dist
