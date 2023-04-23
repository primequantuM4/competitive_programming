class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        occurences = Counter(deck)
        partitionCheck = 0
        for i in occurences.values():
            partitionCheck = self.gcd(i, partitionCheck)

        canBePartitioned = partitionCheck > 1
        return canBePartitioned

    def gcd(self,a, b):
        while b:
            r = a % b
            a = b
            b = r

        return a
