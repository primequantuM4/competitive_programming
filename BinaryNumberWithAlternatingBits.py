class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prevBit = n & 1
        n >>= 1

        while n:
            if prevBit == (n&1):
                return False
            
            prevBit = n & 1
            n>>=1

        return True
