from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def get_idx(char):
            return ord(char) - ord("a")

        if len(p) > len(s):
            return []

        freq = [0] * 26
        target_freq = [0] * 26
        answer = []
        left, right = 0, len(p)

        for char in p:
            target_freq[get_idx(char)] += 1

        for i in range(len(p)):
            char = s[i]
            freq[get_idx(char)] += 1

        if freq == target_freq:
            answer.append(left)

        while right < len(s):
            left_char, right_char = s[left], s[right]

            freq[get_idx(left_char)] -= 1
            freq[get_idx(right_char)] += 1

            left += 1
            right += 1

            if freq == target_freq:
                answer.append(left)

        return answer
