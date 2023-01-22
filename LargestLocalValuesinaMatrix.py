class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0]*(n-2) for _ in range(n-2)]
        for r in range(n-2): 
            for c in range(n-2): 
                ans[r][c] = max(grid[row][col] for row in range(r, r+3) for col in range(c, c+3))
        return ans
