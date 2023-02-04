class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = [0] * 26
        c = [0] * 26

        def get_idx(char):
            return ord(char) - ord("a")

        for char in s1:
            c1[get_idx(char)] += 1

        for i in range(len(s1)):
            char = s2[i]
            c[get_idx(char)] += 1

        left, right = 0, len(s1)

        if c == c1:
            return True

        while right < len(s2):
            c[get_idx(s2[left])] -= 1
            c[get_idx(s2[right])] += 1

            left += 1
            right += 1

            if c == c1:
                return True

        return False
