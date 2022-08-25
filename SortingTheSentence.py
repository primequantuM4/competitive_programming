class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = ""
        wordList = []
        sortedSentence = ""
        for i in s:
            if i == " ":
                totalLength = len(word) - 1
                index = word[totalLength]
                wordList.append(index + word[:totalLength])
                word = ""
                continue
                
            word += i
        totalLength = len(word) - 1
        index = word[totalLength]
        wordList.append(index + word[:totalLength])
        wordList.sort() 
        lastElement = wordList[len(wordList) - 1] 
        for j in wordList[:len(wordList) - 1]:
            sortedSentence += j[1:] + " "
            
        sortedSentence += lastElement[1:] 
        return sortedSentence
