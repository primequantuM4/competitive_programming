class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        min_guy = -1 
        subarray = 0

        for i in nums:
            min_guy &= i
            if min_guy == 0:
                min_guy = -1
                subarray += 1
        return max(1, subarray) 
        