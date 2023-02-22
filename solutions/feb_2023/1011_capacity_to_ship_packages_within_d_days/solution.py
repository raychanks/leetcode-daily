from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total_weight = sum(weights)
        left, right = 1, total_weight

        while left < right:
            mid = (left + right) // 2
            idx = 0

            for _ in range(days):
                capacity_used = 0

                while capacity_used < mid and idx < len(weights):
                    if capacity_used + weights[idx] > mid:
                        break

                    capacity_used += weights[idx]
                    idx += 1

            if idx < len(weights):
                left = mid + 1
            else:
                right = mid

        return left
