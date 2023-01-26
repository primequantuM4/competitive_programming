class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rowSet = set()
        colSet = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rowSet.add(row)
                    colSet.add(col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in rowSet or col in colSet:
                    matrix[row][col] = 0
                
        
