class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_window_size(target, replace):
            start = 0
            max_len = 0
            replaced_count = 0

            for end in range(len(answerKey)):
                if answerKey[end] == target:
                    max_len = max(max_len, end - start + 1)
                    continue

                replaced_count += 1

                while replaced_count > k:
                    if answerKey[start] == replace:
                        replaced_count -= 1
                    start += 1

                max_len = max(max_len, end - start + 1)

            return max_len

        return max(max_window_size("T", "F"), max_window_size("F", "T"))
