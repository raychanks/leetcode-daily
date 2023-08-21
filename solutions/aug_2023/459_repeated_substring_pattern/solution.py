class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False

        for substr_len in range(1, len(s)):
            if len(s) % substr_len != 0:
                continue

            is_repeating = True

            for i in range(substr_len):
                if not is_repeating:
                    break

                j = i
                while j < len(s):
                    if s[j] != s[i]:
                        is_repeating = False
                        break
                    j += substr_len

            if is_repeating:
                return True

        return False
