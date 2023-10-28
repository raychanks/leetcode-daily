class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5

        MOD = 10**9 + 7
        dp = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}

        for _ in range(1, n):
            next_dp = {
                "a": dp["e"] % MOD,
                "e": (dp["a"] + dp["i"]) % MOD,
                "i": (dp["a"] + dp["e"] + dp["o"] + dp["u"]) % MOD,
                "o": (dp["i"] + dp["u"]) % MOD,
                "u": dp["a"] % MOD,
            }
            dp = next_dp

        return sum(dp.values()) % MOD
