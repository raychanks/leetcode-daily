class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        seen_words = set()
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for i, word in enumerate(words):
            char = pattern[i]

            if char not in mapping:
                if word in seen_words:
                    return False
                mapping[char] = word
                seen_words.add(word)
            else:
                if mapping[char] != word:
                    return False

        return True
