import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self._current = 1
        self._min_heap = []
        self._seen_in_heap = set()

    def popSmallest(self) -> int:
        if not self._min_heap:
            result = self._current
            self._current += 1
            return result

        result = heapq.heappop(self._min_heap)
        self._seen_in_heap.remove(result)

        return result

    def addBack(self, num: int) -> None:
        if num >= self._current or num in self._seen_in_heap:
            return

        self._seen_in_heap.add(num)
        heapq.heappush(self._min_heap, num)
