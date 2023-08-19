class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def dp(i):
            if i <= 1:
                return 1
            cur_tree = dp(i-1) * 2 * (2 * i - 1) / (i + 1)
            return int(cur_tree)
        return dp(n)