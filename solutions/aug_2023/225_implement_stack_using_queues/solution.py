from collections import deque


class MyStack:
    def __init__(self):
        self._q = deque([])

    def push(self, x: int) -> None:
        self._q.append(x)
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self) -> int:
        return self._q.popleft()

    def top(self) -> int:
        return self._q[0]

    def empty(self) -> bool:
        return len(self._q) == 0
