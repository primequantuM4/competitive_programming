class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        for i in count.keys():
            if count[i] == 1:
                return i