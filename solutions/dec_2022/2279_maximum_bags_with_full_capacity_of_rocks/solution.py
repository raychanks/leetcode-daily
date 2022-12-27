from typing import List


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        full_count = 0
        non_full = []

        for i in range(len(capacity)):
            if rocks[i] == capacity[i]:
                full_count += 1
            else:
                non_full.append(capacity[i] - rocks[i])

        non_full.sort()

        for remaining in non_full:
            if additionalRocks < remaining:
                break

            full_count += 1
            additionalRocks -= remaining

        return full_count
