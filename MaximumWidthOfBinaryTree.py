# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #append the nulls and the root val
        if not root:
            return 0
        queue = deque()
        queue.append((root, 0))
        max_width = 1

        while queue:
            length = len(queue)
            index_values = []
            for _ in range(length):
                node_value, index = queue.popleft()
                if node_value.left:
                    queue.append((node_value.left, 2*index))

                if node_value.right:
                    queue.append((node_value.right, (2*index) + 1))
                index_values.append(index)

            max_width = max(max_width, index_values[-1] - index_values[0] + 1)
        return max_width
