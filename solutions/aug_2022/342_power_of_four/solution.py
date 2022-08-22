import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return (math.log(n) / math.log(4)).is_integer()

    def pre_compute_is_power_of_four(self, n: int) -> bool:
        """Since -2 ** 31 <= n <= 2 ** 31 - 1, we can pre-compute the possible solutions."""
        return n in {
            1,
            4,
            16,
            64,
            256,
            1024,
            4096,
            16384,
            65536,
            262144,
            1048576,
            4194304,
            16777216,
            67108864,
            268435456,
            1073741824,
        }
