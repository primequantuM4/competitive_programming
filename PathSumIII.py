# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetValueCount = 0
        countedInstances = defaultdict(int)
        countedInstances[0] += 1
        def dfs(root,repeatedInstances, running_sum):
            if not root:
                return
            running_sum += root.val
            self.targetValueCount += repeatedInstances[running_sum - targetSum]
            repeatedInstances[running_sum] += 1
            dfs(root.left, repeatedInstances, running_sum)
            dfs(root.right, repeatedInstances, running_sum)
            repeatedInstances[running_sum] -= 1
        dfs(root, countedInstances, 0)
        return self.targetValueCount
