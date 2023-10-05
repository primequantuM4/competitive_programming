class Solution:
    def knightDialer(self, n: int) -> int:
        adjlist = {
            1: [6,8], 
            2: [7,9], 
            3:[4,8], 
            4: [3,9,0], 
            5: [], 
            6: [1,7,0], 
            7: [2,6], 
            8: [1,3], 
            9: [2,4], 
            0: [4,6]
            }
        @cache
        def dp(remaining, num):
            if remaining == 1:
                return 1
            move_set = 0
            for next_num in adjlist[num]:
                move_set += dp(remaining - 1, next_num)
            
            return move_set
        
        running_sum = 0
        for i in range(10):
            running_sum += dp(n, i)
            
        return running_sum % ((10 ** 9) + 7)





        