class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_counts = [0] * 26

        for i in range(len(words[0])):
            word_counts[ord(words[0][i]) - 97] += 1
        
        for i in range(1, len(words)):
            curr_count = [0] * 26
            for j in range(len(words[i])):
                curr_count[ord(words[i][j]) - 97] += 1
            
            for j in range(26):
                if curr_count[j] < word_counts[j]:
                    word_counts[j] = curr_count[j]
            
        commonCharacters = []
        for i in range(26):
            for j in range(word_counts[i]):
                commonCharacters.append(chr(97+i))
        return commonCharacters
