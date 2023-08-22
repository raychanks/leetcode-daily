from collections import deque


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ORD_A = ord("A")
        LETTER_COUNT = 26
        num = columnNumber
        result = deque([])

        while num > 0:
            div, mod = divmod(num - 1, LETTER_COUNT)
            result.appendleft(chr(mod + ORD_A))
            num = div

        return "".join(result)
