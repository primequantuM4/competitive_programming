class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.movedPath = defaultdict(int)

        directions = [(1, 0), (0, 1)]
        inbound = lambda r, c: 0<=r<m and 0<=c<n

        def dp(current_position):
            if current_position == (m-1, n-1):
                self.movedPath[current_position] += 1
                return self.movedPath[current_position]

            for r, c in directions:
                nr, nc = r + current_position[0], c + current_position[1]
                if (nr, nc) in self.movedPath:
                    self.movedPath[current_position] += self.movedPath[(nr, nc)]
                
                elif (nr, nc) not in self.movedPath and inbound(nr, nc):
                    self.movedPath[current_position] += dp((nr, nc))

            return self.movedPath[current_position]

        return dp((0,0))
                    

            