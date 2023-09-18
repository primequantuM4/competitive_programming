class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dp(left, right):
            if left > right:
                return 0
            if left == right:
                return 1
            curr_palindrome_value = 2 + dp(left + 1, right - 1) if s[left] == s[right] else max(dp(left + 1, right), dp(left, right - 1))
            return curr_palindrome_value
            
        return dp(0, len(s) - 1)
