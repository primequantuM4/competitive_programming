class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result.extend(matrix.pop(0))
            
            if matrix and matrix[0]:
                for subArr in matrix:
                    result.append(subArr.pop())
            if matrix:
                result.extend(matrix.pop() [::-1])
            
            if matrix and matrix[0]:
                for subArr in matrix[::-1]:
                    result.append(subArr.pop(0))
        return result
                
