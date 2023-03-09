class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        nums = [i for i in range(1,n+1)]
        def backtrack(nums,level, k, cur_build):
            if len(cur_build) == k:
                combinations.append(cur_build[:])
                return

            if level == len(nums):
                return

            for i in range(level, len(nums)):
                cur_build.append(nums[i])
                backtrack(nums, i+1, k, cur_build)
                cur_build.pop()

        backtrack(nums, 0, k,[])
        return combinations
