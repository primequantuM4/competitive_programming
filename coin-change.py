class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def solve(remaining_coin):
            if remaining_coin < 0:
                return float('inf')
            if remaining_coin == 0:
                return 0

            min_coins = float('inf')
            for c in coins:
                min_coins = min(min_coins, solve(remaining_coin - c) + 1)
            
            return min_coins

        min_coin = solve(amount)
        return -1 if min_coin == float('inf') else min_coin