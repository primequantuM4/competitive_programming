class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(0, len(s) -1, s)
    
    def reverse(self,start, end, s):
        if start >= end:
            return
        
        s[start], s[end] = s[end], s[start]
        self.reverse(start + 1, end - 1, s)
