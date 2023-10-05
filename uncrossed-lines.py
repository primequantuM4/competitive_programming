class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(left, right):
            if left >= len(nums1) or right >= len(nums2):
                return 0
            
            if nums1[left] == nums2[right]:
                max_val =max(1 + dp(left + 1, right + 1), dp(left, right + 1), dp(left + 1, right))
                return max_val
            
            return max(dp(left + 1, right), dp(left, right + 1))
        
        return dp(0, 0)

        