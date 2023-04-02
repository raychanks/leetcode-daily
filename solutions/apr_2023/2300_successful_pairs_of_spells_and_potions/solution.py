from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        sorted_portions = sorted(potions)
        answer = [0] * len(spells)

        for i, spell in enumerate(spells):
            if spell * sorted_portions[-1] < success:
                continue

            left, right = 0, len(sorted_portions) - 1

            while left < right:
                mid = left + (right - left) // 2

                if sorted_portions[mid] * spell < success:
                    left = mid + 1
                else:
                    right = mid

            answer[i] = len(sorted_portions) - left

        return answer
