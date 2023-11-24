from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix_sum = [0]
        for t in travel:
            prefix_sum.append(prefix_sum[-1] + t)

        # glass, paper, metal
        last_occurance = [0, 0, 0]
        resources = [0, 0, 0]
        for i, g in enumerate(garbage):
            glass_count = g.count("G")
            paper_count = g.count("P")
            metal_count = g.count("M")

            if glass_count:
                last_occurance[0] = max(last_occurance[0], i)
                resources[0] += glass_count

            if paper_count:
                last_occurance[1] = max(last_occurance[1], i)
                resources[1] += paper_count

            if metal_count:
                last_occurance[2] = max(last_occurance[2], i)
                resources[2] += metal_count

        return (
            sum(resources)
            + prefix_sum[last_occurance[0]]
            + prefix_sum[last_occurance[1]]
            + prefix_sum[last_occurance[2]]
        )
