class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def findMinimum(row_index, col_index):
            if row_index == len(triangle) - 1:
                return triangle[row_index][col_index]

            left_side = findMinimum(row_index + 1, col_index)
            right_side = findMinimum(row_index + 1, col_index + 1)

            return min(left_side, right_side) + triangle[row_index][col_index]

        return findMinimum(0, 0)           
