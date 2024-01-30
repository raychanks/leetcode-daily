import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
                continue

            right, left = stack.pop(), stack.pop()

            if t == "+":
                result = left + right
            elif t == "-":
                result = left - right
            elif t == "*":
                result = left * right
            elif t == "/":
                result = math.trunc(left / right)
            else:
                raise ValueError(t)

            stack.append(result)

        return stack[0]
