from collections import deque


class MyQueue:
    def __init__(self):
        self.stack_in = deque()
        self.stack_out = deque()

    def push(self, x: int) -> None:
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())

        self.stack_in.append(x)

    def pop(self) -> int:
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

    def peek(self) -> int:
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out
