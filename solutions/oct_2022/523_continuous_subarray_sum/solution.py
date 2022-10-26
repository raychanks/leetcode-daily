from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_map = {0: 0}
        s = 0

        for i, num in enumerate(nums):
            s += num
            mod = s % k
            if mod not in mod_map:
                mod_map[mod] = i + 1
            elif i - mod_map[mod] >= 1:
                return True

        return False
