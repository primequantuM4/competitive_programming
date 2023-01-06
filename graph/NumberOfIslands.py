class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numberOfIslands = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        inBound = lambda r,c : 0 <= r < len(grid) and 0 <= c < len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    visited.add((row, col))
                    numberOfIslands += 1
                    stack = [(row, col)]
                    while stack:
                        rows, cols = stack.pop()
                        for r, c in directions:
                            nr = r + rows
                            nc = c + cols
                            seen = (nr, nc) in visited
                            if inBound(nr, nc) and (not seen) and grid[nr][nc] == "1":
                                stack.append((nr, nc))
                                visited.add((nr,nc))
        return numberOfIslands
