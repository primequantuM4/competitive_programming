class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cup_filling = defaultdict(int)
        cup_filling[(0, 0)] = poured
        for i in range(query_row + 1):
            for j in range(i + 1):
                overflow = (cup_filling[(i, j)] - 1) / 2
                if overflow > 0:
                    cup_filling[(i + 1, j)] += overflow
                    cup_filling[(i + 1, j + 1)] += overflow
        return min(1, cup_filling[(query_row, query_glass)])


        