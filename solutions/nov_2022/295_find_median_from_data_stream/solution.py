import heapq


class MedianFinder:
    def __init__(self):
        self.smaller = []
        self.larger = []

    def addNum(self, num: int) -> None:
        if not self.larger or self.larger[0] >= num:
            heapq.heappush(self.smaller, -num)
            if len(self.smaller) - len(self.larger) > 1:
                max_in_smaller = -heapq.heappop(self.smaller)
                heapq.heappush(self.larger, max_in_smaller)
            return

        heapq.heappush(self.larger, num)
        if len(self.larger) > len(self.smaller):
            min_in_larger = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -min_in_larger)

    def findMedian(self) -> float:
        if (len(self.smaller) + len(self.larger)) % 2 == 0:
            return (-self.smaller[0] + self.larger[0]) / 2
        else:
            return -self.smaller[0]
