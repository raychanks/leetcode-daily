from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if len(s) < 2:
            return False

        diff_indices = []
        counter = Counter()
        has_same_character = False

        for i in range(len(s)):
            char = s[i]

            counter[char] += 1
            if counter[char] > 1:
                has_same_character = True

            if char == goal[i]:
                continue
            diff_indices.append(i)

        if not diff_indices and has_same_character:
            return True
        if len(diff_indices) != 2:
            return False

        idx1, idx2 = diff_indices
        arr = list(s)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        return "".join(arr) == goal
