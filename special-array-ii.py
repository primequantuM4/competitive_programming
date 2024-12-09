class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        classification = [0]

        for i in range(1, len(nums)):
            if nums[i] % 2 != nums[i - 1] % 2:
                classification.append(classification[-1])
            else:
                classification.append(classification[-1] + 1)

        res = []
        for start, end in queries:
            if classification[start] == classification[end]:
                res.append(True)
            else:
                res.append(False)

        return res
        
