class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        #adding zeros to the top
        pref_matrix = []
        length = len(matrix[0]) + 1
        for r in range(len(matrix) + 1):
            pref_matrix.append([0] * length)
        for r in range(1, len(pref_matrix)):
            for c in range(1, len(pref_matrix[0])):
                pref_matrix[r][c] = matrix[r - 1][c - 1]
            
        for r in range(1, len(pref_matrix)):
            for c in range(1, len(pref_matrix[0])):
                #current
                pref_matrix[r][c] += pref_matrix[r][c-1] - pref_matrix[r-1][c-1] + pref_matrix[r-1][c]
        print(pref_matrix)
        self.pref_matrix = pref_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        subtracted_pref_value = self.pref_matrix[row2 +1][col1] +  self.pref_matrix[row1][col2+1]
        added_pref_value = self.pref_matrix[row2 + 1][col2 + 1] + self.pref_matrix[row1][col1]
        return added_pref_value - subtracted_pref_value

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
