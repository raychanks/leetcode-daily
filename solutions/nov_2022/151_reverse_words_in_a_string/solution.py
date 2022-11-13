import re


class Solution:
    def reverseWords(self, s: str) -> str:
        res = re.findall(r"\w+", s)
        return " ".join(reversed(res))
