class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i+1] = 0
                nums[i] *= 2
        
        #apply moveZeros here
        leftptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[leftptr] = nums[leftptr], nums[i]
                leftptr += 1
        
        return nums
