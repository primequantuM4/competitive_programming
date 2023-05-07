class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        duplicate = -1
        low, high = 1, len(nums) -1

        while low <= high:
            mid = low + (high - low) // 2

            less_nums_count = 0
            for num in nums:
                if num <= mid:
                    less_nums_count += 1

            if less_nums_count > mid:
                duplicate = mid
                high = mid - 1
            
            else:
                low = mid + 1

        return duplicate
