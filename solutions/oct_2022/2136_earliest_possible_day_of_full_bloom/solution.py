from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        optimal_time = 0
        cur_time = 0

        for pt, gt in sorted(
            zip(plantTime, growTime), key=lambda x: (x[1], x[0]), reverse=True
        ):
            cur_time += pt
            optimal_time = max(optimal_time, cur_time + gt)

        return optimal_time
