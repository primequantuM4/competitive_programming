class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.min_cost = float('inf')

        @cache
        def calculate_cost(index):
            if index <= 1:
                return cost[index]
            two_step_cost = calculate_cost(index -2)
            one_step_cost = calculate_cost(index - 1)

            return min(two_step_cost, one_step_cost) + cost[index]
        self.min_cost = min(calculate_cost(len(cost) - 1), calculate_cost(len(cost) - 2)) 

        return self.min_cost