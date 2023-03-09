# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        values_count = defaultdict(int)

        def dfs(root):
            if root is None:
                return

            values_count[root.val] += 1
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        max_frequency = max(values_count.values())
        node_values = values_count.items()

        for values, frequency in node_values:
            if frequency==max_frequency:
                res.append(values)
        return res
