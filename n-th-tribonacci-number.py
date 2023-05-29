class Solution:
    def tribonacci(self, n: int) -> int:
        self.number_map = defaultdict(int)

        def dp(n):
            if n == 2 or n == 1:
                return 1
            if n == 0:
                return 0

            if n in self.number_map:
                return self.number_map[n]
            
            self.number_map[n] = dp(n-1) + dp(n-2) + dp(n-3)
            return self.number_map[n]

        return dp(n)
