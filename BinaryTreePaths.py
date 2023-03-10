# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #working approach: find next and append to array
        self.possible_paths = []

        def backtrack(path, root):
            if root.left:
                path.append(str(root.left.val))
                backtrack(path, root.left)
                path.pop()
            if root.right:
                path.append(str(root.right.val))
                backtrack(path, root.right)
                path.pop()
            if not root.right and not root.left:
                self.possible_paths.append("->".join(path[:]))
                return
        backtrack([str(root.val)], root)
        return self.possible_paths
