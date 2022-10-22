from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        char_set = set(t)
        left, right = 0, 0
        counter_window = Counter()
        res = ""

        while right <= len(s):
            window_contains = True
            for char in char_set:
                if counter_window[char] < counter_t[char]:
                    window_contains = False
                    break

            if window_contains:
                if not res or right - left < len(res):
                    res = s[left:right]
                char = s[left]
                counter_window[char] -= 1
                left += 1
            else:
                if right >= len(s):
                    break
                char = s[right]
                counter_window[char] += 1
                right += 1

        return res
