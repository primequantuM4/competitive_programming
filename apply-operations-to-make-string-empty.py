        dict_count = Counter(s)
        max_num = max(dict_count.values())
        dict_count = {k:v for k, v in dict_count.items() if v == max_num}
        res = ""
        for i in s:
            if i not in dict_count:
                continue
            if dict_count[i] == 1:
                res += i
            dict_count[i] -= 1
        
        return res
    def lastNonEmptyString(self, s: str) -> str:
class Solution: