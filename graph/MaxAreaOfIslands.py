class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    cur_area = 0
                    stack = [(row, col)]
                    visited.add((row, col))
                    while stack:
                        rows, cols = stack.pop()
                        cur_area += 1
                        for r, c in directions:
                            next_row = r + rows
                            next_col = c + cols
                            seen = (next_row, next_col) in visited
                            if inBound(next_row, next_col) and (not seen) and grid[next_row][next_col] == 1:
                                stack.append((next_row, next_col))
                                visited.add((next_row, next_col))
                    max_area = max(cur_area, max_area)
        return max_area
