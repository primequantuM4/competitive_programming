class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points_and_cost = []
        representative = {}
        value_sums = 0

        def manhattan(point_a, point_b):
            return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

        def union(x, y):
            x_rep, y_rep = find(x), find(y)
            if x_rep == y_rep:
                return
            
            representative[y_rep] = representative[x_rep]

        def find(x):
            while x != representative[x]:
                representative[x] = representative[representative[x]]
                x = representative[x]

            return x
        
        for i in range(len(points)):
            representative[tuple(points[i])] = tuple(points[i])
            for j in range(i+1, len(points)):
                cost_for_connecting = manhattan(points[i], points[j])
                point = [tuple(points[i]), tuple(points[j]), cost_for_connecting]
                points_and_cost.append(point)

        points_and_cost.sort(key= lambda x: x[-1])
        for p1, p2, score in points_and_cost:
            p1_rep, p2_rep = find(p1), find(p2)
            if p1_rep != p2_rep:
                value_sums += score
                union(p1_rep, p2_rep)

        
        return value_sums