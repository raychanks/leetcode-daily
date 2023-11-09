from functools import cache


class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7

        @cache
        def calc_ways(n):
            if n <= 1:
                return n
            return (calc_ways(n - 1) + n) % MOD

        ways = 0
        cur_char = ""
        consecutive_count = 0

        for char in s:
            if char == cur_char:
                consecutive_count += 1
            else:
                ways = (ways + calc_ways(consecutive_count)) % MOD
                cur_char = char
                consecutive_count = 1

        return (ways + calc_ways(consecutive_count)) % MOD
