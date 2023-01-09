from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        total_damage = sum(damage)

        return total_damage + 1 - min(max_damage, armor)
