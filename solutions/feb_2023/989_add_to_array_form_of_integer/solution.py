from collections import deque
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = deque()
        k_str = str(k)
        carry = 0

        for i in range(max(len(num), len(k_str))):
            digit1 = num[len(num) - 1 - i] if i < len(num) else 0
            digit2 = int(k_str[len(k_str) - 1 - i]) if i < len(k_str) else 0

            digit_sum = carry + digit1 + digit2

            if digit_sum > 9:
                carry = 1
                result.appendleft(digit_sum - 10)
            else:
                carry = 0
                result.appendleft(digit_sum)

        if carry:
            result.appendleft(carry)

        return list(result)
