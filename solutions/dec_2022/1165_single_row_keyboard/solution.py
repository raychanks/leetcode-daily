class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        idx_map = {char: idx for idx, char in enumerate(keyboard)}
        time_needed = 0
        cur_pos = 0

        for char in word:
            dest = idx_map[char]
            time_needed += abs(dest - cur_pos)
            cur_pos = dest

        return time_needed
