class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []

        for row in range(len(matrix)):
            for col in range(len(matrix)):
                heappush(nums,-1 * matrix[row][col])
        while len(nums) > k:
            heappop(nums)

        return -1 * nums[0]
