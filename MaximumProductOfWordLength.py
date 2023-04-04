class Solution:
    def maxProduct(self, words: List[str]) -> int:
        strValues = defaultdict(int)
        maxValues = 0
        for word in words:
            for char in word:
                strValues[word] |= (1<<(ord(char) - 97))

        
        for word in range(len(words) - 1):
            for second in range(word + 1, len(words)):
                if strValues[words[word]] & strValues[words[second]] == 0:
                    maxValues = max(maxValues, len(words[word]) * len(words[second]))

        
        return maxValues
