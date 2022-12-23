class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        ideal_outcome = 0
        for i in range(1, len(nums) + 1):
            ideal_outcome += i
        return ideal_outcome - total_sum
