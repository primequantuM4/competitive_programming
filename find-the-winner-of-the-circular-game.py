class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = []
        for player in range(1, n+1):
            players.append(player)
        
        countedPlayers = 1
        playerIndex = 0

        while len(players) > 1:
            if countedPlayers == k:
                countedPlayers = 0
                players.pop(playerIndex)
                playerIndex -= 1
            playerIndex = (playerIndex + 1) % len(players)
            countedPlayers += 1
        
        return players[0]