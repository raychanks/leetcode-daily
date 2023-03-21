from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def get_count_by_length(length):
            # arithmetic sequence
            return (1 + length) * length // 2

        count = 0
        cur_len = 0

        for num in nums:
            if num == 0:
                cur_len += 1
            else:
                count += get_count_by_length(cur_len)
                cur_len = 0

        count += get_count_by_length(cur_len)

        return count
