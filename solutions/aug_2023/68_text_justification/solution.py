from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        cur_len = 0

        for word in words:
            if cur_len + len(word) > maxWidth:
                result.append(self.justify(line, maxWidth))
                line = []
                cur_len = 0

            line.append(word)
            cur_len += len(word) + 1

        if line:
            result.append(" ".join(line).ljust(maxWidth))

        return result

    def justify(self, words, maxWidth):
        if len(words) == 1:
            return words[0].ljust(maxWidth)

        total_len = sum(len(word) for word in words)
        total_spaces = maxWidth - total_len
        div, mod = divmod(total_spaces, len(words) - 1)
        result = []

        for word in words:
            result.append(word)
            num_spaces = div + 1 if mod > 0 else div
            mod -= 1
            result.append(" " * num_spaces)

        return "".join(result[:-1])
