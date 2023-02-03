class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = []
        for _ in range(numRows):
            rows.append([])

        is_increasing = True
        row_idx = 0
        for char in s:
            rows[row_idx].append(char)

            if is_increasing and row_idx == numRows - 1:
                is_increasing = False
            elif not is_increasing and row_idx == 0:
                is_increasing = True

            if is_increasing:
                row_idx += 1
            else:
                row_idx -= 1

        result = ""
        for row in rows:
            result += "".join(row)

        return result
