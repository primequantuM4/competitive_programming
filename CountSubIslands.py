class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        totalSubSetLand = 0

        def inBound(r, c):
            return 0 <= r <len(grid1) and 0 <= c < len(grid1[0])

        def dfs(start):
            stack = []
            stack.append(start)
            isASubLand = True
            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            while stack:
                cur_row, cur_col = stack.pop()
                if grid1[cur_row][cur_col] != 1:
                    isASubLand = False

                for r, c in directions:
                    next_row, next_col = cur_row + r, cur_col + c
                    isLand = inBound(next_row, next_col) and grid2[next_row][next_col] == 1

                    if isLand:
                        grid2[next_row][next_col] = 2
                        stack.append((next_row, next_col))

            return isASubLand
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1:
                    grid2[row][col] = 2
                    isASubLand = bfs((row, col))
                    if isASubLand:
                        totalSubSetLand += 1

        return totalSubSetLand 


