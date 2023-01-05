class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        #use a stack I guess
        addedSpaceResult = []
        sentence = list(map(str, s))
        while spaces:
            indexToBeAdded = spaces.pop()
            word = []
            while sentence and len(sentence) > indexToBeAdded:
                addedSpaceResult.append(sentence.pop())
            addedSpaceResult.append(" ")

        while sentence:
            addedSpaceResult.append(sentence.pop())
        return "".join(addedSpaceResult[::-1])
