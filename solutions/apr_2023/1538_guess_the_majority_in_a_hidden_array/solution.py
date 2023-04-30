# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
# 	 # Compares 4 different elements in the array
# 	 # return 4 if the values of the 4 elements are the same (0 or 1).
# 	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
# 	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
# 	 # Returns the length of the array
#    def length(self) -> int:
#


class ArrayReader:
    def __init__(self, arr) -> None:
        self.arr = arr

    def length(self):
        return len(self.arr)

    def query(self, a, b, c, d):
        count_0, count_1 = 0, 0

        for i in (a, b, c, d):
            if self.arr[i] == 0:
                count_0 += 1
            else:
                count_1 += 1

        if count_0 == count_1:
            return 0
        if count_0 == 4 or count_1 == 4:
            return 4
        return 2


class Solution:
    def guessMajority(self, reader: "ArrayReader") -> int:
        result = [-1] * reader.length()
        result[0] = 0

        zero_to_three = reader.query(0, 1, 2, 3)
        one_to_four = reader.query(1, 2, 3, 4)

        if zero_to_three == one_to_four:
            result[4] = result[0]
        else:
            result[4] = result[0] ^ 1

        for i in range(1, 4):
            args = [num for num in range(5) if num != i]
            q = reader.query(*args)
            xor = 0 if q == one_to_four else 1
            result[i] = result[0] ^ xor

        for i in range(1, len(result) - 4):
            if reader.query(i, i + 1, i + 2, i + 3) == reader.query(
                i + 1, i + 2, i + 3, i + 4
            ):
                result[i + 4] = result[i]
            else:
                result[i + 4] = result[i] ^ 1

        idx_0, idx_1 = -1, -1
        count_0, count_1 = 0, 0
        for idx, num in enumerate(result):
            if num == 0:
                count_0 += 1
                idx_0 = idx
            else:
                count_1 += 1
                idx_1 = idx

        if count_0 > count_1:
            return idx_0
        elif count_0 < count_1:
            return idx_1
        else:
            return -1
