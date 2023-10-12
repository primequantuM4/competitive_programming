class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        ans = 1
        for i in range(1, n + 1):
            ans *= (2 * i - 1)
        
        ans = factorial(n) * ans
        return ans % mod
        
        