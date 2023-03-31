class Solution:
    def maxA(self, n: int) -> int:
        states = {}

        def solve(steps_left, cur_len, buffer_len):
            if steps_left < 0:
                return 0

            if steps_left == 0:
                return cur_len

            state = (steps_left, cur_len, buffer_len)

            if state in states:
                return states[state]

            if buffer_len <= 1:
                states[state] = max(
                    # press A
                    solve(steps_left - 1, cur_len + 1, buffer_len),
                    # ctrl a + ctrl c
                    solve(steps_left - 2, cur_len, cur_len),
                )
            else:
                states[state] = max(
                    # ctrl a + ctrl c
                    solve(steps_left - 2, cur_len, cur_len),
                    # ctrl v
                    solve(steps_left - 1, cur_len + buffer_len, buffer_len),
                )

            return states[state]

        return solve(n, 0, 0)
