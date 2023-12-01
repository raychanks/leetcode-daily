from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        m, n = len(word1), len(word2)
        ptr1, sub_ptr1 = 0, 0
        ptr2, sub_ptr2 = 0, 0

        while ptr1 < m and ptr2 < n:
            if word1[ptr1][sub_ptr1] != word2[ptr2][sub_ptr2]:
                return False

            sub_ptr1 += 1
            sub_ptr2 += 1

            if sub_ptr1 == len(word1[ptr1]):
                ptr1 += 1
                sub_ptr1 = 0

            if sub_ptr2 == len(word2[ptr2]):
                ptr2 += 1
                sub_ptr2 = 0

        return ptr1 == m and ptr2 == n
