class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(row, col):
            stack = []
            stack.append((row, col))

            area = 1
            grid[row][col] = 2
            inBound = lambda r, c: 0 <= r< len(grid) and 0 <= c < len(grid[0])

            directions = [(1,0), (0,1), (-1,0), (0,-1)]

            while stack:
                cur_row, cur_col = stack.pop()

                for r, c in directions:
                    next_row = cur_row + r
                    next_col = cur_col + c
                    isLand = inBound(next_row, next_col) and grid[next_row][next_col] == 1
                    
                    if isLand:
                        grid[next_row][next_col] = 2
                        area += 1
                        stack.append((next_row, next_col))

            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))

        return maxArea
