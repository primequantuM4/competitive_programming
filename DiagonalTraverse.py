class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r, c = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        for i in range(r * c):
            result.append(mat[row][col])
            if (row + col) % 2 == 0:
                if col == c - 1: 
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            else:
                if row == r - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    col -= 1
                    row += 1
        return result
