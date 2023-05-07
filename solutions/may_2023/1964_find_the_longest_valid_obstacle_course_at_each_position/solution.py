import bisect
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        result = [0] * len(obstacles)
        dp = [10**9] * (len(obstacles) + 1)

        for i, num in enumerate(obstacles):
            index = bisect.bisect(dp, num)
            result[i] = index + 1
            dp[index] = num

        return result
