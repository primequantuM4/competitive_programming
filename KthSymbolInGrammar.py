class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            #basecase
            return 0

        if k%2!=0:
            #odd numbered
            valueForK = self.kthGrammar(n-1, (k+ 1) // 2)
            return valueForK
        else:
            #even numbered
            valueForK = (self.kthGrammar(n-1, k // 2) + 1) % 2
            return valueForK
            
