import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue = []
        cur_time = 0
        sorted_tasks = sorted(
            [[*val, idx] for idx, val in enumerate(tasks)], key=lambda x: x[0]
        )
        ordering = []
        i = 0

        while i < len(sorted_tasks):
            available_at, process_time, idx = sorted_tasks[i]

            if not queue:
                cur_time = max(cur_time, available_at)
                heapq.heappush(queue, (process_time, idx))
                i += 1
                continue

            if cur_time >= available_at:
                heapq.heappush(queue, (process_time, idx))
                i += 1
                continue

            task = heapq.heappop(queue)
            ordering.append(task[1])
            cur_time += task[0]

        while queue:
            task = heapq.heappop(queue)
            ordering.append(task[1])

        return ordering
