class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        stringNumbers = "0123456789"
        stringToNum = {}
        for i in range(len(stringNumbers)):
            stringToNum[stringNumbers[i]] = i
        #change num 1 and num 2 to string
        int1 = self.changeToInt(len(num1), num1, stringToNum)
        int2 = self.changeToInt(len(num2), num2, stringToNum)

        return str(int1 * int2)
    def changeToInt(self, digit: int, num: str, dictionary) -> int:
        digit -= 1
        res = 0
        for i in num:
            res += dictionary[i] * (10 ** digit)
            digit -= 1
        return res
