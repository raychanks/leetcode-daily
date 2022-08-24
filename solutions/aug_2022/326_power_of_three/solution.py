import math


# -(2 ** 31) <= n <= 2 ** 31 - 1
MAX_POWER_IN_RANGE = math.floor(math.log(2**31 - 1, 3))


# cannot use log(n) / log(3) due to precision issue


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (3**MAX_POWER_IN_RANGE) % n == 0
