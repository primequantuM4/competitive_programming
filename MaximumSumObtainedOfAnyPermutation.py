class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        #first try to find the maximum intersections 
        #sort it based on the number of intersections -> reversed
        max_sum = 0
        nums.sort()
        sweep = [0] * len(nums)
        for start, end in requests:
            sweep[start] += 1
            if end < len(nums) - 1:
                sweep[end + 1] -= 1

        sweep[0] = (sweep[0], 0)

        for i in range(1, len(sweep)):
            sweep[i] += sweep[i-1][0]
            sweep[i] = (sweep[i], i)
        
        sweep.sort(reverse=True)

        for i in range(len(sweep)):
            repeat, idx = sweep[i]
            nums[idx], nums[-1-i] = nums[-1-i], nums[idx]

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        #calculate the sum
        for start, end in requests:
            value_subtracted = nums[start - 1] if start > 0 else 0
            max_sum += nums[end] - value_subtracted

        return (max_sum) % ((10 ** 9) + 7)
