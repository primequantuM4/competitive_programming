# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counted_instance = defaultdict(int)
        counted_instance[0] += 1
        possible_path_count = 0
        
        def dfs(node, running_sum):
            nonlocal possible_path_count
            if not node:
                return
            
            running_sum += node.val

            possible_path_count += counted_instance[running_sum - targetSum]
            counted_instance[running_sum] += 1

            dfs(node.left, running_sum)
            dfs(node.right, running_sum)

            counted_instance[running_sum] -= 1
        
        dfs(root, 0)
        return possible_path_count

        