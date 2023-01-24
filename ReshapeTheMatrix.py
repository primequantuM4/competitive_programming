class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        colLength = len(mat[0])
        calculatedIndex = 0
        if not mat or r * c != len(mat) * len(mat[0]):
            return mat
        answer =  [[0 for x in range(c)] for y in range(r)]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                answer[calculatedIndex // c][calculatedIndex % c] = mat[row][col]
                calculatedIndex +=1
        
        return answer
