class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        inbound = lambda r,c : 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        @cache
        def dp(row, col):
            if row == len(matrix) - 1:
                return matrix[row][col]
            left = float('inf') if not inbound(row + 1, col - 1) else dp(row + 1, col - 1)
            mid = dp(row + 1, col)
            right = float('inf') if not inbound(row + 1, col + 1) else dp(row + 1, col + 1)
            return min(left, mid, right) + matrix[row][col]
        
        min_value = float('inf')
        for i in range(len(matrix[0])):
            min_value = min(min_value, dp(0, i))
        
        return min_value