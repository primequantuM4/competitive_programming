class Solution:
    def isPalindrome(self, x: int) -> bool:
        #first find the digit length
        if (x < 0): 
            return False
        num = x
        count = 0
        while num != 0:
            count += 1
            num = num //10
        num = x
        sums = 0
        while count > 0:
            var = num % 10
            count -= 1
            sums += var * (10 ** count)
            num = num//10
        return sums == x
