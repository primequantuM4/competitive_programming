class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window
        min_sum_length = len(nums) + 1
        left = 0
        value = 0
        for right in range(len(nums)):
            value += nums[right]

            while value >= target:
                min_sum_length = min(min_sum_length, right - left + 1)
                value -= nums[left]
                left += 1
        
        if min_sum_length == len(nums) + 1:
            return 0
        return min_sum_length
