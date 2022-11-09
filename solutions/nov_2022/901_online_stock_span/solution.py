from collections import deque


class StockSpanner:
    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        count = 1
        while self.stack:
            last_price, last_count = self.stack.pop()
            if price >= last_price:
                count += last_count
            else:
                self.stack.append((last_price, last_count))
                self.stack.append((price, count))
                return count
        self.stack.append((price, count))
        return count
