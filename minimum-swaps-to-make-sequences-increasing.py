class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = [-1] + nums1, [-1] + nums2
        @cache
        def dp(i, is_swapped):
            if i >= len(nums1):
                return 0
            
            value = inf
            if is_swapped:
                if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                    value = min(value, dp(i + 1, False))
                
                if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                    value = min(value, dp(i + 1, True) + 1)
                
            
            else:
                if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                    value = min(value, dp(i + 1, False))
                
                if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                    value = min(value, dp(i + 1, True) + 1)

            return value
        
        return dp(1, False)