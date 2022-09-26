from typing import List

from templates.dsu import DSU


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        char_sets = [DSU.make_set(chr(ord("a") + i)) for i in range(26)]

        for equation in equations:
            a, b = equation[0], equation[-1]
            is_equal = equation[1] == "="
            idx_a, idx_b = ord(a) - ord("a"), ord(b) - ord("a")

            if is_equal:
                set_a, set_b = char_sets[idx_a], char_sets[idx_b]
                DSU.union(set_a, set_b)

        for equation in equations:
            a, b = equation[0], equation[-1]
            is_equal = equation[1] == "="
            idx_a, idx_b = ord(a) - ord("a"), ord(b) - ord("a")

            if not is_equal:
                set_a, set_b = char_sets[idx_a], char_sets[idx_b]
                if DSU.find_set(set_a) is DSU.find_set(set_b):
                    return False

        return True
