class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonString = strs[0]
        for index in range(1, len(strs)):
            while strs[index].find(commonString) != 0:
                commonString = commonString[:len(commonString) - 1]
        return commonString
