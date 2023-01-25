class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxVal = set()
        colVal = set()
        for row in range(len(board)):
            rowVal = set()
            for col in range(len(board[0])):
                boxIndex = (row // 3) * 3 + (col // 3)
                value = board[row][col]
                if (col,value) in colVal or value in rowVal or (boxIndex, value) in boxVal:
                    return False
                if board[row][col] != ".":
                    colVal.add((col, value))
                    rowVal.add(value)
                    boxVal.add((boxIndex, value)) 
        return True
