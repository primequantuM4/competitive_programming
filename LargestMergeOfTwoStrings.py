class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        firstBlock = deque(map(str, word1))
        secondBlock = deque(map(str, word2))
        merge = []

        ptr1, ptr2 = 0, 0

        while ptr1 < len(word1) and ptr2 < len(word2):
            if firstBlock >= secondBlock:
                merge.append(firstBlock.popleft())
                ptr1 += 1
            else:
                merge.append(secondBlock.popleft())
                ptr2 += 1

        while firstBlock:
            merge.append(firstBlock.popleft())

        while secondBlock:
            merge.append(secondBlock.popleft())    

        return "".join(merge)        
