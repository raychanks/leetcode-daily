from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        num_neg = 0

        for i in range(32):
            bit_sum = 0

            for num in nums:
                bit = (num >> i) & 1
                bit_sum += bit

            result |= (bit_sum % 3) << i

        for num in nums:
            if num < 0:
                num_neg += 1

        if num_neg % 3 == 0:
            return result
        return result - 2**32
