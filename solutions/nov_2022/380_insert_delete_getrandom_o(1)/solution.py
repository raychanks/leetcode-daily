import random


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.idx_map = {}

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False

        self.arr.append(val)
        idx = len(self.arr) - 1
        self.idx_map[val] = idx

        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False

        last_val = self.arr[-1]
        val_idx = self.idx_map[val]

        self.arr[val_idx], self.arr[-1] = self.arr[-1], self.arr[val_idx]
        self.arr.pop()

        self.idx_map[last_val] = val_idx
        del self.idx_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
