class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_len = 0
        answer = ""

        for i in range(n):
            cur_len = 1
            cur_width = 0

            for w in range(1, n):
                if i - w not in range(n) or i + w not in range(n):
                    break

                if s[i - w] == s[i + w]:
                    cur_len += 2
                    cur_width = w
                else:
                    break

            if cur_len > longest_len:
                longest_len = cur_len
                answer = s[i - cur_width : i + cur_width + 1]

        for i in range(n - 1):
            if s[i] != s[i + 1]:
                continue

            cur_len = 2
            cur_width = 0

            for w in range(1, n):
                if i - w not in range(n) or i + 1 + w not in range(n):
                    break

                if s[i - w] == s[i + 1 + w]:
                    cur_len += 2
                    cur_width = w
                else:
                    break

            if cur_len > longest_len:
                longest_len = cur_len
                answer = s[i - cur_width : i + 1 + cur_width + 1]

        return answer
