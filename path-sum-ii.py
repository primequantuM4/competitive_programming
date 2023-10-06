# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        valid_path = []
        stack = [(root, root.val)]
        parent = {root: - 1}

        while stack:
            cur_node, running_sum = stack.pop()
            if not cur_node.left and not cur_node.right and running_sum == targetSum:
                valid_path.append(self.getPath(parent, cur_node)) 
            
            if cur_node.left:
                stack.append((cur_node.left, running_sum + cur_node.left.val))
                parent[cur_node.left] = cur_node
            
            if cur_node.right:
                stack.append((cur_node.right, running_sum + cur_node.right.val))
                parent[cur_node.right] = cur_node

        return valid_path
    
    def getPath(self, parent, node):
        ans = []
        while node in parent:
            ans.append(node.val)
            node = parent[node]
        return ans[::-1]