class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1, count2 = [0] * 26, [0] * 26

        for i in range(len(word1)):
            index1, index2 = ord(word1[i]) - 97, ord(word2[i]) - 97

            count1[index1] += 1
            count2[index2] += 1
        
        for i in range(len(count1)):
            if count1[i] == 0 and count2[i] > 0 or count1[i] > 0 and count2[i] == 0:
                return False
        count1.sort()
        count2.sort()

        return count1 == count2 
        
