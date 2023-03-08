# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([])
        queue.append(root)
        res = []

        if not root:
            return res
        
        while queue:
            #get length of queue
            length = len(queue)
            inner_res = []
            for _ in range(length):
                value = queue.popleft()
                inner_res.append(value.val)

                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
            
            res.append(inner_res)
        return res
