class Solution:
    def maxFrequency(self, nums, k):
        nums.sort()
        sums = 0
        i = 0
        frequency = 0
        for j in range(len(nums)):
            sums += nums[j]
            while nums[j]*(j-i+1) > sums+k:
                sums -= nums[i]
                i = i+1
            frequency = max(frequency, j-i+1)
        return frequency
