import heapq


class SeatManager:
    def __init__(self, n: int):
        self.marker = 1
        self.min_heap = []

    def reserve(self) -> int:
        if self.min_heap:
            return heapq.heappop(self.min_heap)
        seat = self.marker
        self.marker += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.min_heap, seatNumber)
