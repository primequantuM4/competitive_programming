class Solution(object):
    def reverseString(self, s, i=1):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        size = ((len(s) - 1) // 2) + 1
        if len(s) % 2 == 0:
            size = len(s)/ 2 
        if i-1 == size:
                return
        s[len(s) - i], s[i-1] = s[i - 1], s[len(s) - i]
        i += 1
        self.reverseString(s, i)
