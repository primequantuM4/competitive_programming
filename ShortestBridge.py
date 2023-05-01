class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid)

        def bfs(start):
            queue = deque([start])
            visited = {start}

            while queue:
                cr, cc = queue.popleft()
                for r, c in directions:
                    nr, nc = cr + r, cc + c
                    valid_cell = inbound(nr, nc) and (nr, nc) not in visited
                    if valid_cell and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return visited

        first_island = set()

        for row in range(len(grid)):
            for col in range(len(grid)):
                if not first_island and grid[row][col] == 1:
                    first_island = first_island.union(bfs((row, col)))
                    break

        position = deque(list(first_island))
        level = 0
        while position:
            length = len(position)
            for _ in range(length):
                row,col = position.popleft()

                for r, c in directions:
                    nr, nc = r + row, c + col
                    valid_cell = inbound(nr, nc) and (nr, nc) not in first_island
                    if valid_cell and grid[nr][nc] == 0:
                        position.append((nr, nc))
                        first_island.add((nr, nc))

                    elif valid_cell and grid[nr][nc] == 1:
                        return level

            level += 1
