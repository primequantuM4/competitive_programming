class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        @cache
        def dp(i, taken):
            
            take, skip = values[i] + dp(i + 1, taken + 1), dp(i + 1, taken)
            if taken == 1:
            if taken >= 2:
                return 0
                take -= i
            else:
                take += i
            
            return max(take, skip)
            if i >= len(values):
                return -inf