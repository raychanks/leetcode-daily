from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        max_score = 0
        score = 0

        while left <= right:
            smaller_token = tokens[left]
            larger_token = tokens[right]

            if power >= smaller_token:
                power -= smaller_token
                score += 1
                max_score = max(max_score, score)
                left += 1
            elif score == 0:
                break
            else:
                power += larger_token
                score -= 1
                right -= 1

        return max_score
