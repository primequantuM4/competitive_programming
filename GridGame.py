class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        #pref sum
        top,bottom = grid

        for i in range(1, len(grid[0])):
            top[i] += top[i-1]
            bottom[i] += bottom[i-1]

        res = float('inf')
        for i in range(len(grid[0])):
            row1 = top[-1] - top[i]
            row2 = bottom[i - 1] if i > 0 else 0
            optimalPath = max(row1, row2)
            res = min(res, optimalPath)

        return res
