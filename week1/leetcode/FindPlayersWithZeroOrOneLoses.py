class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        recordsOfWinnings = collections.defaultdict(int)
        recordsOfLoss = collections.defaultdict(int)
        
        result = []
        winners = []
        losers = []

        for winner, loser in matches:
            recordsOfWinnings[winner] += 1
            recordsOfLoss[loser] += 1
        
        for player in recordsOfWinnings:
            if recordsOfLoss[player] == 0:
                winners.append(player)
        
        for player in recordsOfLoss:
            if recordsOfLoss[player] == 1:
                losers.append(player)
        
        losers.sort()
        winners.sort()

        result.append(winners)
        result.append(losers)

        return result 

