class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest_num = min(nums)
        largest_num = max(nums)
        
        while smallest_num != 0:
            remainder = largest_num % smallest_num
            largest_num = smallest_num
            smallest_num = remainder
        
        return largest_num
