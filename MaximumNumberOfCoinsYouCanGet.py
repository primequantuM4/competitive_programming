class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        maxSumOfOutput = 0
        maxRange = (len(piles)//3) - 1
        endList = len(piles)
        for i in range(2, len(piles) - maxRange, 2):
            maxSumOfOutput += piles[endList - i]
        return maxSumOfOutput
