from collections import defaultdict


class MyCalendarThree:
    def __init__(self):
        self.differentials = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.differentials[start] += 1
        self.differentials[end] -= 1

        max_k, k = 0, 0
        items = sorted(self.differentials.items(), key=lambda x: x[0])
        for _, count in items:
            k += count
            max_k = max(max_k, k)

        return max_k
