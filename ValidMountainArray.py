class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #find max index
        if len(arr) < 3 or arr == sorted(arr) or arr[::-1] == sorted(arr):
            return False
        maxIndex = 0
        for i in range(1, len(arr)):
            if arr[maxIndex] < arr[i]:
                maxIndex = i
            if arr[i] == arr[i-1]:
                return False
        
        if arr[:maxIndex + 1] == sorted(arr[:maxIndex + 1]) and arr[maxIndex:][::-1] == sorted(arr[maxIndex:]):
            return True
        return False
