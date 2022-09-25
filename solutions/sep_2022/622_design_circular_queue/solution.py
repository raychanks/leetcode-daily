class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.data = [0] * k
        self.size = 0
        self.front_idx = 0
        self.rear_idx = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.data[self.rear_idx] = value
        self.rear_idx = (self.rear_idx + 1) % self.k
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front_idx = (self.front_idx + 1) % self.k
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.data[self.front_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        idx = (self.rear_idx + self.k - 1) % self.k
        return self.data[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
