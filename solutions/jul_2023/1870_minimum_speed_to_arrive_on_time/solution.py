import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        upper_speed = 10**7
        left, right = 1, upper_speed

        while left <= right:
            speed = (left + right) // 2
            time_taken = 0

            for distance in dist:
                time_taken = math.ceil(time_taken)
                time_taken += distance / speed

            if time_taken > hour:
                left = speed + 1
            else:
                right = speed - 1

        return left if left <= upper_speed else -1
