class Solution:
    def maxScore(self, nums: List[int]) -> int:
        self.max_score = 0

        @cache
        def dp(mask):
            if mask == (2 ** len(nums)) - 1:
                return 0
            
            max_score = 0

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    i_pos = 1 <<  len(nums) - i - 1
                    j_pos =  1 <<  len(nums) - j - 1
                    if mask & i_pos==0 and mask & j_pos == 0:
                        val_i = nums[i]
                        val_j = nums[j]
                        cur_mask = mask | i_pos | j_pos
                        op = bin(cur_mask).count("1") // 2

                        s = dp(cur_mask) + self.calculate(op, val_i, val_j)
                        max_score = max(s, max_score)

            return max_score 
            
        return dp(0)
   
    
    def calculate(self, i, a, b):
        return i * math.gcd(a, b)

