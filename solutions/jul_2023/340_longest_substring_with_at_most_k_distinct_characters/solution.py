from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
        max_len = 0
        start = 0

        for end in range(len(s)):
            char = s[end]
            counter[char] += 1

            while len(counter) > k:
                leaving = s[start]

                if counter[leaving] == 1:
                    del counter[leaving]
                else:
                    counter[leaving] -= 1

                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
