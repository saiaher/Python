class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current = 0
        down = True

        for ch in s:
            rows[current] += ch

            if current == 0:
                down = True
            elif current == numRows - 1:
                down = False

            if down:
                current += 1
            else:
                current -= 1

        return "".join(rows)