from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        attack_desc = sorted(properties, key=lambda x: x[0], reverse=True)
        weak_character_count = 0
        max_defense_so_far = 0
        cur_max_defense = 0
        previous_attack = 0

        for attack, defense in attack_desc:
            if attack != previous_attack:
                max_defense_so_far = max(max_defense_so_far, cur_max_defense)
                cur_max_defense = defense
            else:
                cur_max_defense = max(cur_max_defense, defense)

            if defense < max_defense_so_far:
                weak_character_count += 1

            previous_attack = attack

        return weak_character_count
