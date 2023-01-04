class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        maxOutputArea = 0
        nums.sort()
        for i in range(len(nums) - 2):
            max_index = i
            tot_perimeter = 0
            for j in range(i, i + 3):
                tot_perimeter += nums[j]
                if nums[max_index] < nums[j]:
                    max_index = j
            tot_perimeter -= nums[max_index]
            if nums[max_index] < tot_perimeter:
                maxOutputArea = max(tot_perimeter + nums[max_index], maxOutputArea)
            
        return maxOutputArea
