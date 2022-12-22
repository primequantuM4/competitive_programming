class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #approach -> use a hashmap to store a key value pair of numbers and it's count
        #Then use a simple mathematics calculation to find how many pairs it can have
        number_mapping = Counter(nums)
        pairs = 0
        for values in number_mapping.values():
            pairs += (values * (values - 1)) // 2
        return pairs
