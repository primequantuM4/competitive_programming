class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        max_sequence = 1
        for num in arr:
            exsisting_num = dp[num - difference]
            dp[num] = exsisting_num + 1
            max_sequence = max(max_sequence, dp[num])

        return max_sequence

