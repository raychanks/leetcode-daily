class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        prime_factors = {2, 3, 5}

        while n > 1 and prime_factors:
            pf = prime_factors.pop()
            while n % pf == 0 and n > 1:
                n //= pf

        return n == 1
