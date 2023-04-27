# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        averageArray = []
        queue = deque([root])

        while queue:
            length = len(queue)
            value = 0
            for _ in range(length):
                cur_node = queue.popleft()
                value += cur_node.val

                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)

            averageVal = value / length
            averageArray.append(averageVal)


        return averageArray
