class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        bit_shift = 1
        next_inc = 2
        result = 0

        for i in range(1, n + 1):
            if i == next_inc:
                next_inc *= 2
                bit_shift += 1

            result = (result << bit_shift | i) % mod

        return result
