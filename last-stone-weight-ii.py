class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def dp(index, curr_weight):
            if index == len(stones):
                return abs(curr_weight)
            return min(dp(index + 1, curr_weight + stones[index]), dp(index + 1, curr_weight - stones[index]))
        
        return dp(0, 0)
