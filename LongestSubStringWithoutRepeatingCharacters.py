class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rememberingList = set()
        maxSubStringLength = 0
        left = 0
        for right in s:
            while right in rememberingList:
                rememberingList.remove(s[left])
                left += 1
            rememberingList.add(right)
            maxSubStringLength = max(maxSubStringLength, len(rememberingList))
        return max(maxSubStringLength, len(rememberingList))
