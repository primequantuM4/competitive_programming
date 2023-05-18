class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        path = {
            1: {(0, -1), (0, 1)},
            2: {(1, 0), (-1, 0)},
            3: {(0, -1), (1, 0)},
            4: {(1, 0), (0, 1)},
            5: {(-1, 0), (0, -1)},
            6: {(-1, 0), (0, 1)}
        }
        #check both ways If they are connected
        n, m = len(grid), len(grid[0])
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        queue = deque([(0, 0)])
        visited = {(0, 0)}

        while queue:
            row, col = queue.popleft()
            if (row, col) == (n - 1, m -1):
                return True

            for r, c in path[grid[row][col]]:
                nr, nc = r + row, c + col
                if inbound(nr, nc) and (-1 *r, -1 * c) in path[grid[nr][nc]] and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))

        return False

            