class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        visited_combinations = set()
        subsequences = []
        def backtrack(level, possible_combo):
            if len(possible_combo) >= 2 and tuple(possible_combo) not in visited_combinations:
                subsequences.append(possible_combo[:])
                visited_combinations.add(tuple(possible_combo[:]))

            for i in range(level, len(nums)):
                canAppend = len(possible_combo) == 0 or possible_combo[-1] <= nums[i]
                if canAppend:
                    possible_combo.append(nums[i])
                    backtrack(i+1, possible_combo)
                    possible_combo.pop()

        backtrack(0, [])
        return subsequences
