class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * (len(nums) + 1), [1]* (len(nums) + 1)
        #build the left
        for i in range(len(nums)):
            left[i] *= nums[i] * left[i - 1]

        #build the right
        for i in range(len(nums) - 1, -1, -1):
            right[i] *= nums[i] * right[i+1]

        #product here
        for i in range(len(nums)):
            nums[i] = left[i - 1] * right[i + 1]
        
        return nums
            
