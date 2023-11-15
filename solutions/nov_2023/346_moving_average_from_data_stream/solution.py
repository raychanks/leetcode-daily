from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.data = deque([])
        self.sum = 0

    def next(self, val: int) -> float:
        self.data.append(val)
        self.sum += val

        if len(self.data) > self.size:
            leaving = self.data.popleft()
            self.sum -= leaving

        return self.sum / len(self.data)
