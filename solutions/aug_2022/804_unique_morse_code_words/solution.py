from typing import List


class Solution:
    MORSE_MAP = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_str_set = set()

        for word in words:
            morse_str = ""
            for char in word:
                morse_idx = ord(char) - ord("a")
                morse_str += Solution.MORSE_MAP[morse_idx]
            morse_str_set.add(morse_str)

        return len(morse_str_set)
