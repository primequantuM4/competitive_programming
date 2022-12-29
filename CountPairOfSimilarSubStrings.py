class Solution:
    def similarPairs(self, words: List[str]) -> int:
        compare_arr = []
        res = 0
        for i in words:
            out = set()
            for j in i:
                out.add(j)
            compare_arr.append(out)
        res = 0
        for i in range(len(compare_arr) - 1):
            compared_set = compare_arr[i]
            for j in range(i+1, len(compare_arr)):
                if compared_set == compare_arr[j]:
                    res+=1
            
        return res
