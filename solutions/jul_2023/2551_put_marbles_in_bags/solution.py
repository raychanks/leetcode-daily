from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        cuts = []

        for i in range(len(weights) - 1):
            cuts.append(weights[i] + weights[i + 1])

        cuts.sort()
        min_cost = sum(cuts[: k - 1])
        max_cost = sum(cuts[len(cuts) - (k - 1) :])

        return max_cost - min_cost
