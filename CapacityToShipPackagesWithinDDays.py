class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #find the possible ranges 
        #first possible range is the last element of the array and last possible is the sum of the weights 

        low = max(weights)
        high = sum(weights)
        
        min_capacity = 51
        while low <= high:
            capacity = low + (high - low) // 2

            usedDays = self.numberOfDays(capacity, weights)
            
            if usedDays > days:
                low = capacity + 1
            elif usedDays <= days:
                high = capacity - 1
                min_capacity = capacity
        
        return min_capacity

    def numberOfDays(self, capacity, weights):
        days = 0
        value = 0
        for i in range(len(weights)):
            value += weights[i]

            if value > capacity:
                days += 1
                value = weights[i]

        if value:
            days += 1
            
        return days
    

        




