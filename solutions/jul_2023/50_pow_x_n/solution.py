from functools import cache


class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x

        num = abs(n)

        if num % 2 == 0:
            result = self.myPow(x, num // 2) * self.myPow(x, num // 2)
        else:
            result = self.myPow(x, num // 2) * self.myPow(x, num // 2) * x

        return 1 / result if n < 0 else result
