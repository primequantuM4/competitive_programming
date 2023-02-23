class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if(len(p) > len(s)):
            return []
        counter_p = Counter(p)
        window_dict = defaultdict(int)
        start,end = 0,0
        index_anagram = []
        for  i in range(len(p)):
            window_dict[s[end]] += 1
            end += 1
        if window_dict == counter_p:
            index_anagram.append(start)

        while end < len(s):
            window_dict[s[end]] += 1
            window_dict[s[start]] -= 1

            if (window_dict[s[start]] == 0):
                del(window_dict[s[start]])
            start += 1
            end += 1

            if window_dict == counter_p:
                index_anagram.append(start)

        return index_anagram




        
