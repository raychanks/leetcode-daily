from collections import Counter
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        res = [0, 0]

        for i in range(1, len(nums) + 1):
            if s[i] == 2:
                res[0] = i
            elif s[i] == 0:
                res[1] = i

        return res
