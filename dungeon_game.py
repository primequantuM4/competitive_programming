class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        goal = (len(dungeon) - 1, len(dungeon[0]) - 1)
        inbound = lambda r, c: 0 <= r < len(dungeon) and 0 <= c < len(dungeon[0])
        @cache
        def dp(row, col):
            if (row, col) == goal:
                if dungeon[row][col] <= 0:
                    return abs(dungeon[row][col]) + 1
                return 1
            down = float('inf') if not inbound(row + 1, col) else dp(row + 1, col)
            right = float('inf') if not inbound(row, col + 1) else dp(row, col + 1)

            fast_path = -dungeon[row][col] + min(down, right)
            return  fast_path if fast_path > 0 else 1
        hit_value = dp(0, 0)
        return hit_value if hit_value != float('inf') else 1

        
