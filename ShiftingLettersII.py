class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_value = {0 : -1,1 : 1}

        shift = [0] * (len(s) + 1)
        ans = list(map(str, s))
        for start, end, val in shifts:
            shift[start] += shift_value[val]
            shift[end + 1] -= shift_value[val]

        #apply prefix sum
        for i in range(1, len(s)):
            shift[i] += shift[i - 1]

        shift.pop()
        for i in range(len(s)):
            val = ord(ans[i]) - 97 
            val = (26 + (val + shift[i])) % 26

            ans[i] = chr(val + 97)

        return "".join(ans)
            



