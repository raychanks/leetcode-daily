import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        profit_max_heap = []
        pairs = sorted(
            [(profits[i], capital[i]) for i in range(n)],
            key=lambda x: (x[1], -x[0]),
        )

        cur_capital = w
        num_taken = 0
        idx = 0

        while num_taken < k and num_taken < n:
            while idx < len(pairs) and pairs[idx][1] <= cur_capital:
                heapq.heappush(profit_max_heap, (-pairs[idx][0], -pairs[idx][1]))
                idx += 1

            if not profit_max_heap:
                break

            next_project = heapq.heappop(profit_max_heap)
            cur_capital += -next_project[0]
            num_taken += 1

        return cur_capital
