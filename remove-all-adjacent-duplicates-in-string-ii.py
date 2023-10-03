class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["", -1]]
        for i in s:
            if i == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([i, 1])
        
        ans = ""
        for sub, val in stack:
            ans += (sub * val)
        
        return ans