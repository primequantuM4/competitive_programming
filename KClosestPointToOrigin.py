class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = [0]
        # points.sort()
        distanceLength = []
        for i in range(len(points) - 1):
            for j in range(len(points) - i - 1):
                # previousDistance = ((points[j - 1][0] ** 2) + (points[j - 1][1] ** 2)) ** 0.5
                # firstDistance = 
                # secondDistance = 
                if ((points[j][0] ** 2) + (points[j][1] ** 2)) ** 0.5 > ((points[j + 1][0] ** 2) + (points[j + 1][1] ** 2)) ** 0.5:
                    points[j], points[j+1] = points[j+1], points[j]           
        for j in range(k):
            distanceLength.append(points[j])
        
        return distanceLength
    
