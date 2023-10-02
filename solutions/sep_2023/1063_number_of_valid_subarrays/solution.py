import math
from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        rmq = RMQ(nums)
        count = len(nums)

        for i in range(len(nums) - 1):
            left, right = i + 1, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[i] <= rmq.query(i + 1, mid):
                    left = mid + 1
                else:
                    right = mid - 1
            count += left - i - 1

        return count


class RMQ:
    def __init__(self, nums) -> None:
        self.sparse_table = self.build_table(nums)

    def build_table(self, nums):
        sparse_table = [nums]

        exp = 1
        while 2**exp <= len(nums):
            range_mins = []
            for i in range(len(nums) + 1 - 2**exp):
                range_left_min = sparse_table[exp - 1][i]
                range_right_min = sparse_table[exp - 1][i + 2 ** (exp - 1)]
                range_min = min(range_left_min, range_right_min)
                range_mins.append(range_min)
            sparse_table.append(range_mins)
            exp += 1

        return sparse_table

    def query(self, start, end) -> int:
        range_size = end - start + 1
        exp = math.floor(math.log2(range_size))

        range_left_min = self.sparse_table[exp][start]
        range_right_min = self.sparse_table[exp][end + 1 - 2**exp]

        return min(range_left_min, range_right_min)
