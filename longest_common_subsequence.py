class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def longest_common(ptr1, ptr2):
            if ptr1 >= len(text1) or ptr2 >= len(text2):
                return 0
            
            if text1[ptr1] == text2[ptr2]:
                chain =  1 + longest_common(ptr1 + 1, ptr2 + 1)

            else:
                chain = max(longest_common(ptr1 + 1, ptr2), longest_common(ptr1, ptr2 + 1))        
            
            return chain
        
        return longest_common(0, 0)
