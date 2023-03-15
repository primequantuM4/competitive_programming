class Solution:
    def decodeString(self, s: str) -> str:
        res, value = self.decodeAndMultiply(s, 0)
        return res
    def decodeAndMultiply(self,s,index):
        returnedValue = ""
        number = ""

        while index < len(s):
            if s[index] == "]":
                #base case
                return returnedValue, index

            elif s[index] == "[":
              inner_string, paused_index = self.decodeAndMultiply(s, index+1)
              index = paused_index
              returnedValue +=  (inner_string * int(number))
              number = ""
            elif s[index].isdigit():
                number += s[index]
            else:
                returnedValue += s[index]
            index += 1

        return returnedValue, index
