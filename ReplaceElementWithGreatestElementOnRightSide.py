class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = arr[-1]
        for i in reversed(range(len(arr)-1)):
            if max_element <= arr[i]:
                arr[i], max_element = max_element, arr[i]
            else:
                arr[i] = max_element
            
        arr[-1] = -1
        return arr
