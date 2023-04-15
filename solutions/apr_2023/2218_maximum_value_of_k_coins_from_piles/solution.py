from functools import cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        prefix_sums = []

        for pile in piles:
            prefix_sum = [0] * (len(pile) + 1)
            cur = 0

            for i, num in enumerate(pile, start=1):
                cur += num
                prefix_sum[i] = cur

            prefix_sums.append(prefix_sum)

        @cache
        def solve(pile_idx, k_left):
            if k_left == 0 or pile_idx == len(piles):
                return 0

            pile = piles[pile_idx]
            max_val = 0

            for j in range(len(pile) + 1):
                if j > k_left:
                    break

                max_val = max(
                    max_val,
                    prefix_sums[pile_idx][j] + solve(pile_idx + 1, k_left - j),
                )

            return max_val

        return solve(0, k)
