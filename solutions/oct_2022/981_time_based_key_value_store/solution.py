from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        values = self.data[key]
        if values[0][0] > timestamp:
            return ""

        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            ts, v = values[mid]
            if ts == timestamp:
                return v
            if ts < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return values[left - 1][1]
