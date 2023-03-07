from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, 10**14

        while left < right:
            mid = left + (right - left) // 2
            count = 0

            for t in time:
                count += mid // t

            if count >= totalTrips:
                right = mid
            else:
                left = mid + 1

        return left
