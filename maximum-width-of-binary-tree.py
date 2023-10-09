# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 1
        
        max_width = 1
        queue = deque([(root, 0)])

        while queue:
            length = len(queue)
            min_index = inf
            max_index = -inf
            for _ in range(length):
                node, index = queue.popleft()
                min_index = min(min_index, index)
                max_index = max(max_index, index)

                if node.left:
                    queue.append((node.left, 2 * index))
                
                if node.right:
                    queue.append((node.right, 2 * index +1))
                
            max_width = max(max_width, max_index - min_index + 1)
        return max_width 

        