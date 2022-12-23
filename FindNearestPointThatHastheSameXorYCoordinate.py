class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_value = float('inf')
        min_index = -1

        for i in range(len(points)):
            coords = points[i]
            coordX, coordY = coords
            if coordX == x or coordY == y:
                manhattanDistance = abs(x - coordX) + abs(y - coordY)
                if manhattanDistance < min_value:
                    min_value = manhattanDistance
                    min_index = i

        return min_index
