class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deletedCols = 0
        
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                wordPrev = strs[row - 1]
                curWord = strs[row]
                if curWord[col] < wordPrev[col]:
                    deletedCols += 1
                    break
        return deletedCols
        
