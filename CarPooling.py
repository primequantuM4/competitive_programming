class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #first find the max so that we can build the array
        if len(trips) == 1:
            return trips[0][0] <= capacity
        length = 1

        for pas_num, start, end in trips:
            length = max(start, end, length)

        travelled_trip = [0] * (length + 2)

        #doing the query instruction
        for pas_num, start, end in trips:
            travelled_trip[start] += pas_num
            travelled_trip[end] += -1 * pas_num

        #apply pref sum
        for i in range(len(travelled_trip)):
            travelled_trip[i] += travelled_trip[i-1] 
            if travelled_trip[i] > capacity:
                return False
        return True
        
