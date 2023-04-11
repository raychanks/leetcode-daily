from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        res = deque()
        skip = 0

        for i in range(len(s) - 1, -1, -1):
            char = s[i]

            if char == "*":
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                res.appendleft(char)

        return "".join(res)
