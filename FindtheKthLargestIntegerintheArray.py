class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = []
        for i in nums:
            arr.append(int(i))
        arr.sort()
        return str(arr[len(arr) - k])
