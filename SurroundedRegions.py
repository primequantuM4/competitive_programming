class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visited = set()
        edges = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or r == len(board) - 1:
                    edges.add((r, c))
                elif c == 0 or c == len(board[0]) - 1:
                    edges.add((r, c))

        def flip(arr):
            for r,c in arr:
                board[r][c] = 'X'

        def dfs(coord):
            start_row, start_col = coord
            flipped = [(start_row, start_col)]
            stack = [(start_row, start_col)]
            can_be_flipped = True

            while stack:
                cr, cc = stack.pop()
                for r, c in directions:
                    nr, nc = cr + r, c + cc
                    valid = self.inBound(board, (nr, nc)) and (nr, nc) not in visited
                    if valid and board[nr][nc] == 'O':
                        visited.add((nr, nc))
                        stack.append((nr, nc))
                        flipped.append((nr, nc))

                    if (nr, nc) in edges and board[nr][nc] == 'O':
                        can_be_flipped = False

            return can_be_flipped, flipped

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r, c) not in visited  and board[r][c] == 'O':
                    visited.add((r, c))
                    node_flip = (r, c) not in edges
                    flipped, coordinates = dfs((r, c))
                    if flipped and node_flip:
                        flip(coordinates)



    def inBound(self, board, coord):
        row, col = coord
        return 0 <= row < len(board) and 0<= col < len(board[0])
