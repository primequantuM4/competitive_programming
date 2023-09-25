class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dp(index, time):
            if index > len(satisfaction) - 1:
                return 0
            
            return max(satisfaction[index] * time + dp(index + 1, time + 1), dp(index + 1, time))
        
        return dp(0, 1)
