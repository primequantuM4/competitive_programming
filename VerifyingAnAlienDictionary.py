class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        indexAlien = {}
        for index, value in enumerate(order):
            indexAlien[value] = index
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                     return False

                if words[i][j] != words[i + 1][j]:
                    if indexAlien[words[i][j]] > indexAlien[words[i+1][j]]:
                        return False
                    break

        return True
