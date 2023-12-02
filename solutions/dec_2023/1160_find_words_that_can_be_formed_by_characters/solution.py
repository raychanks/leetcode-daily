from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        answer = 0

        for word in words:
            if Counter(word) < counter:
                answer += len(word)

        return answer
