from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        stack = []

        for start, end in intervals:
            if not stack:
                stack.append([start, end])
                continue

            prev_start, prev_end = stack[-1]

            if prev_start <= start <= prev_end:
                stack.pop()
                stack.append([prev_start, max(prev_end, end)])
            else:
                stack.append([start, end])

        return stack
