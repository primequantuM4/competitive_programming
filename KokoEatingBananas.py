class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxEatingSpeed =  max(piles)

        #do binary search
        low = 1
        high = maxEatingSpeed

        wantedEatingSpeed = 0

        while low <= high:
            eatingSpeed = low + (high - low) // 2

            eatingTime = self.eatingTime(eatingSpeed, piles)
            if eatingTime > h:
                low = eatingSpeed + 1
            else:
                high = eatingSpeed - 1
                wantedEatingSpeed = eatingSpeed

        return wantedEatingSpeed

    def eatingTime(self, eatingSpeed, piles):
        hours = 0

        for bananna in piles:
            hours += (ceil(bananna / eatingSpeed))

        return hours
