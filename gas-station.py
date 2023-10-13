class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #we have a list of potential index
        #check that potential index if it can travel the world
        #if it can, then, we found a solution since it's unique
        total_gain = 0
        curr_gain = 0
        res = 0

        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            if curr_gain < 0:
                curr_gain = 0
                res = i + 1
        
        return res if total_gain >= 0 else -1

        