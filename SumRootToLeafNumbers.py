# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        path_val = []

        while stack:
            node, cur_tracked_digit = stack.pop()
            cur_tracked_digit = (cur_tracked_digit * 10) + node.val 
            
            if not node.left and not node.right:
                path_val.append(cur_tracked_digit)

            if node.left:
                stack.append((node.left, cur_tracked_digit))
            
            if node.right:
                stack.append((node.right, cur_tracked_digit))

        
        return sum(path_val)
