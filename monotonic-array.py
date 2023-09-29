class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        is_increasing = nums[0] <= nums[-1]
        for i in range(1, len(nums)):
            if is_increasing and nums[i] < nums[i - 1]:
                return False
            elif not is_increasing and nums[i] > nums[i - 1]:
                return False
        return True 
        