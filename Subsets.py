class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #one guarantee is that all non-empty elements will always have an empty element as their subset
        possible_subsets = []
        def backtrack(subset, level):
            #everything is a solution
            possible_subsets.append(subset[:])

            for i in range(level, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i+1)
                subset.pop()

        backtrack([], 0)
        return possible_subsets
