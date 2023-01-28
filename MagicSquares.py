class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        magicGrids = 0
        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) -2):
                subGrid = [grid[i][col:col+3] for i in range(row, row+3)]
                isValidGrid = self.checkIfMagic(subGrid)
                if isValidGrid:
                    magicGrids += 1
        return magicGrids
        

    def  checkIfMagic(self,grid):
        row = [0]*3
        col = [0]*3
        diagonal = 0
        antidiagonal = 0
        repeatedRecord = set()
        for r in range(3):
            for c in range(3):
                if grid[r][c] < 1 or grid[r][c] > 9 or grid[r][c] in repeatedRecord:
                    return False
                repeatedRecord.add(grid[r][c])
        for r in range(3):
            for c in range(3):
                row[r] += grid[r][c]
                col[c] += grid[r][c]
                if r == c:
                    diagonal += grid[r][c]
                if c == 3 - 1 - r:
                    antidiagonal += grid[r][c]
        
        horizontalLength = collections.Counter(row)
        verticalLength = collections.Counter(col)

        lengthOne = len(horizontalLength) == 1 and len(verticalLength) == 1
        sameValue = row[0] == col[0] and col[0] == antidiagonal and diagonal == antidiagonal

        if lengthOne and sameValue:
            return True
        return False

