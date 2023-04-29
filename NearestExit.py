class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        exits = set()
        n, m = len(maze), len(maze[0])
        ex, ey = entrance
        maze[ex][ey] = "+"
        
        def isBorder(r, c):
            on_col_edge = c == 0  or c == m - 1
            on_row_edge = r == 0 or r == n - 1

            return on_row_edge or on_col_edge


        def inbound(r, c):
            return 0<=r<n and 0<=c<m

        def bfs(start_node):
            queue = deque([start_node])
            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            visited = {start_node}
            while queue:
                row, col, level = queue.popleft()

                if isBorder(row, col) and maze[row][col] == ".":
                    return level

                for r, c in directions:
                    nr, nc = r + row, c + col
                    valid_state = (nr, nc) not in visited and inbound(nr, nc)
                    if valid_state and maze[nr][nc] == ".":
                        visited.add((nr, nc))
                        queue.append((nr, nc, level + 1))

            return -1


        return(bfs((ex, ey, 0)))




