from collections import deque


class MyQueue:
    def __init__(self):
        self._stack_in = deque()
        self._stack_out = deque()

    def push(self, x: int) -> None:
        self._stack_in.append(x)

    def pop(self) -> int:
        self._reverse_stack()
        return self._stack_out.pop()

    def peek(self) -> int:
        self._reverse_stack()
        return self._stack_out[-1]

    def empty(self) -> bool:
        return not self._stack_in and not self._stack_out

    def _reverse_stack(self):
        if not self._stack_out:
            while self._stack_in:
                self._stack_out.append(self._stack_in.pop())
