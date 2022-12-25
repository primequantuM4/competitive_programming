class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            # traverse each index and check if the 3rd chr is a '#'
            # if it is, it tells us that the value we're changing is above i
            if i < len(s) - 2 and s[i + 2] == "#":
                # changing the value from a number to a letter
                res += chr(int(s[i] + s[i + 1]) + 96)
                i += 2
            else:
                res += chr(int(s[i]) + 96)
            i += 1
        return res
        
