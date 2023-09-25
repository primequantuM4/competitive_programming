class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = [(scores[i], ages[i]) for i in range(len(ages))]
        players.sort(key=lambda x: (x[1],x[0]))

        @cache
        def dp(i):
            if i == 0:
                return players[0][0]

            max_value = players[i][0]

            for j in range(i - 1, -1, -1):
                if players[i][0] >= players[j][0]:
                    score = dp(j)
                    max_value = max(players[i][0] + score, max_value)

            return max_value

        cur_max = 1
        
        for i in range(len(players)):
            cur_max = max(dp(i), cur_max)

        return cur_max
