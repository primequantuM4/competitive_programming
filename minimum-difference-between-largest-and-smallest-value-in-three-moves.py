class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        minimized_difference = float('inf')

        minimized_difference = min(minimized_difference, nums[-1] - nums[3])
        minimized_difference = min(minimized_difference, nums[-4] - nums[0])
        minimized_difference = min(minimized_difference, nums[-2] - nums[2])
        minimized_difference = min(minimized_difference, nums[-3] - nums[1])


        return minimized_difference