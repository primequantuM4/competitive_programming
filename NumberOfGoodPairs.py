class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #approach -> use a hashmap to store a key value pair of numbers and arr
        #when we use arr we can know the number of times that each element has in the array
        number_mapping = {}
        number_values = []
        for i in range(len(nums)):
            if nums[i] not in number_mapping:
                number_mapping[nums[i]] = [i]
                number_values.append(nums[i])
            else:
                number_mapping[nums[i]].append(i)
            
        res = 0
        for i in number_values:
            res += (len(number_mapping[i]) * (len(number_mapping[i]) - 1)) // 2
        return res

        

