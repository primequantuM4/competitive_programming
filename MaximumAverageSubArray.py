class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if (len(nums) == 1):
            return float(nums[0])
        maxAvg = 0
        for start in range(0,len(nums) - k +1):
            currSum = 0
            for end in range(start,start+k):
                currSum += nums[end]
            maxAvg =  max(maxAvg, currSum/k)
        return maxAvg
