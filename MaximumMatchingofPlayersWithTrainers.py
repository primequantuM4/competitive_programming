class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        #sort the trainer first
        trainers.sort()
        players.sort()
        trainers = collections.deque(trainers)

        pairedUp= 0

        for i in players:
            while trainers and trainers[0] < i:
                trainers.popleft()
            if trainers:
                pairedUp += 1
                trainers.popleft()
            else:
                break
        
        return pairedUp
