from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete_count = 0

        for col in range(len(strs[0])):
            prev_char = "a"

            for row in range(len(strs)):
                char = strs[row][col]

                if char < prev_char:
                    delete_count += 1
                    break

                prev_char = char

        return delete_count
