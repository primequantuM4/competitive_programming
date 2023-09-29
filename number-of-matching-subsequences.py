class Solution: 
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index = -1
        index_mapping = defaultdict(list)

        for idx, char in enumerate(s):
            index_mapping[char].append(idx)
        
        value = 0
        for word in words:
            index = 0
            for i in word:
                pos = bisect_left(index_mapping[i], index)
                if pos < len(index_mapping[i]):
                    index = index_mapping[i][pos] + 1

                else:
                    value -= 1
                    break
            value += 1            
        
        return value