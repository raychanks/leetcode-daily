class Solution:
    def countAndSay(self, n: int) -> str:
        say = "1"

        for _ in range(2, n + 1):
            tmp = ""
            cur = say[0]
            count = 0
            for char in say:
                if char != cur:
                    tmp += f"{count}{cur}"
                    cur = char
                    count = 1
                else:
                    count += 1
            tmp += f"{count}{cur}"
            say = tmp

        return say
