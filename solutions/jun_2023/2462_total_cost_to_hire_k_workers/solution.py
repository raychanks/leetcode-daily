import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = 0, len(costs) - 1
        min_heap = []

        for _ in range(candidates):
            if left > right:
                break

            if left == right:
                heapq.heappush(min_heap, (costs[left], left))
                left += 1
                break

            heapq.heappush(min_heap, (costs[left], left))
            heapq.heappush(min_heap, (costs[right], right))

            left += 1
            right -= 1

        total_cost = 0

        for _ in range(k):
            cost, index = heapq.heappop(min_heap)
            total_cost += cost

            if left > right:
                continue

            if index < left:
                heapq.heappush(min_heap, (costs[left], left))
                left += 1
            elif index > right:
                heapq.heappush(min_heap, (costs[right], right))
                right -= 1

        return total_cost
