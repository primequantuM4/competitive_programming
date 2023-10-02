class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_num = 0
        running_sum = 0

        for i in range(len(nums)):
            running_sum += nums[i]

            max_num = max(max_num, ceil((running_sum) / (i + 1)))
        
        return max_num
