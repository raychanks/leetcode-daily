from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        prev_end = -(10**9)
        remove_count = 0

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
                continue

            if prev_end > end:
                prev_end = end

            remove_count += 1

        return remove_count
