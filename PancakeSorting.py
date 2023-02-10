class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for max_number in range(len(arr), 1, -1):
            indexOfMaxNumber = arr.index(max_number)
            res.extend([indexOfMaxNumber + 1, max_number])
            arr = arr[:indexOfMaxNumber:-1] + arr[:indexOfMaxNumber]
        return res
