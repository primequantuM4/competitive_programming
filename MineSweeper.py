class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        cur_row, cur_col = click
        directions = [(1,0), (0,1), (-1,0), (0,-1),(1,1), (-1,1), (1,-1), (-1,-1)]
        if board[cur_row][cur_col] == 'M':
            board[cur_row][cur_col] = 'X'
            return board

        number_of_bombs, emptySpot = self.count_bombs_and_empty_spots(cur_row, cur_col, board)
        if number_of_bombs:
            board[cur_row][cur_col] = str(number_of_bombs)
            return board

        board[cur_row][cur_col] = 'B'
        for r, c in emptySpot:
            self.updateBoard(board, [r, c])

        return board
      
    def count_bombs_and_empty_spots(self, r, c, board):
        directions = [(1,0), (0,1), (-1,0), (0,-1),(1,1), (-1,1), (1,-1), (-1,-1)]
        number_of_bombs = 0
        emptySpot = []
        for cr, cc in directions:
            nr, nc = r + cr, cc + c
            is_a_bomb = self.in_bound(board, nr, nc) and board[nr][nc] == 'M'
            if is_a_bomb:
                number_of_bombs += 1
            elif self.in_bound(board, nr, nc) and board[nr][nc] == 'E':
                emptySpot.append((nr, nc))

        return number_of_bombs, emptySpot
        
    def in_bound(self, board, r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0])
