class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(buffer_size):
            if buffer_size == 1:
                return 0
            value = buffer_size #considering one to be a factor
            for num in self.get_factors(buffer_size):
                paste_buffer_step = int(buffer_size / num - 1)
                copy_step = 1
                steps = dp(num)
                value = min(value, steps + paste_buffer_step + copy_step)
            return value
        return dp(n) 
            
    def get_factors(self, n):
        factors = []
        for factor in range(1, n // 2):
            if n % factor == 0:
                factors.append(factor)
        return factors


        
