class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        n = len(grid)

        def inBound(r, c):
            return 0 <= r < n and 0 <= c < n

        queue = deque([(0, 0, 1)])
        visited = set()

        while queue:
            row, col, level = queue.popleft()

            if (row, col) == (n - 1, n- 1):
                return level

            for r, c in directions:
                nr, nc = r + row, c + col
                is_valid = inBound(nr, nc) and (nr, nc) not in visited
                
                if is_valid and grid[nr][nc] == 0:
                    queue.append((nr, nc, level + 1))
                    visited.add((nr, nc))

        return -1
        
