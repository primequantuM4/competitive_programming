# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Keep track of the max node to the path below
        # Have a global count that tracks the node status
        self.good_node_count = 0

        def traverse(node, point_so_far):
            if not node:
                return
            
            if node.val >= point_so_far:
                self.good_node_count += 1
            
            traverse(node.left, max(node.val, point_so_far))
            traverse(node.right, max(node.val, point_so_far))
        
        traverse(root, -float('inf'))
        return self.good_node_count
        
