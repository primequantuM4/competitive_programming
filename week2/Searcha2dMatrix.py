class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first create a 1D int arr so that we can implement binary search on it 
        oneDMatrixLength = len(matrix) * len(matrix[0])
        truthValue = self.binarySearch(matrix, oneDMatrixLength, target)
        return truthValue
    def binarySearch(self,matrix, totalLength, target):
        left = 0
        right = totalLength - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
