# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximumSum = -1001
        def dfs(root):
            if root is None: # found a leaf node so return
                return 0

            # make two calls towards left and right
            left_call = max(dfs(root.left), 0)
            right_call = max(dfs(root.right), 0)

            left_sum, right_sum = left_call + root.val, right_call + root.val
            total_sum = left_call + right_call + root.val

            optimum_sum = max(left_sum, right_sum)
            self.maximumSum = max(self.maximumSum, total_sum)

            return optimum_sum

        dfs(root)
        return self.maximumSum
