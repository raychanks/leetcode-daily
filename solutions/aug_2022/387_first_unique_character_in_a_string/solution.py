class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = {}

        for idx, char in enumerate(s):
            if char in char_map:
                char_map[char] = len(s) + 1
            else:
                char_map[char] = idx

        first_uniq_idx = min(char_map.values())

        return first_uniq_idx if first_uniq_idx < len(s) else -1
