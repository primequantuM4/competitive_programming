class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        if len(banned) == n:
            return 0

        banned_set = set(banned)
        res = 0 
        curr_sum = 0

        for i in range(1, n + 1):
            if i in banned_set:
                continue

            if curr_sum + i > maxSum:
                break
            
            curr_sum += i
            res += 1
        
        return res
            
            
