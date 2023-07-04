# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        max_money = 0
        @cache
        def steal(node):
            if node is None:
                return (0, 0)

            left = steal(node.left)
            right = steal(node.right)

            stealed_version = node.val + left[1] + right[1]
            non_steal_version = max(left) + max(right)

            return [stealed_version, non_steal_version]
            
            

        return max(steal(root))