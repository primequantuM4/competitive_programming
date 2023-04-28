class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[float('inf') for col in range(len(row))] for row in mat]
        queue = deque()
        directions = [(1, 0),(0, 1), (-1, 0), (0, -1)]

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    ans[row][col] = 0
                    queue.append((row, col))

        def inBound(r, c):
            return 0<=r<len(mat) and 0<=c<len(mat[0])


        while queue:
            row, col = queue.popleft()


            for r, c in directions:
                nr, nc = r + row, c + col
                if inBound(nr, nc) and ans[nr][nc] > ans[row][col] + 1:
                    ans[nr][nc] = ans[row][col] + 1
                    queue.append((nr, nc))



        return ans

                
