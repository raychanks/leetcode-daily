from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)

        if counter_t - counter_s:
            return ""

        left, right = 0, 1
        min_str = s
        counter = Counter(s[0])

        while left < len(s):
            if counter_t - counter:
                if right < len(s):
                    counter[s[right]] += 1
                    right += 1
                else:
                    break
            else:
                if right - left < len(min_str):
                    min_str = s[left:right]
                counter[s[left]] -= 1
                left += 1

        return min_str
