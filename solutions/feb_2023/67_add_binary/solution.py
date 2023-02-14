from collections import deque


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = deque()
        la, lb = len(a), len(b)
        carry = 0

        for i in range(max(la, lb)):
            digit_a = int(a[la - 1 - i]) if i < la else 0
            digit_b = int(b[lb - 1 - i]) if i < lb else 0

            sum_ab = digit_a ^ digit_b ^ carry
            carry = (digit_a & digit_b) | (digit_b & carry) | (carry & digit_a)

            result.appendleft(str(sum_ab))

        if carry != 0:
            result.appendleft(str(carry))

        return "".join(result)
