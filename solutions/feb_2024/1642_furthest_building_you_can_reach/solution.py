import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        height_diff = []
        bricks_used = 0
        idx = 0

        for i in range(len(heights) - 1):
            height_diff.append(heights[i + 1] - heights[i])

        for diff in height_diff:
            if diff <= 0:
                idx += 1
                continue

            if len(min_heap) < ladders:
                heapq.heappush(min_heap, diff)
                idx += 1
                continue

            if ladders and min_heap[0] < diff:
                bricks_used += heapq.heapreplace(min_heap, diff)
            else:
                bricks_used += diff

            if bricks_used <= bricks:
                idx += 1
            else:
                break

        return idx
