# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        #define our dictionary
        if root is None:
            return []
        values_col = defaultdict(list)
        res = []
        queue = deque()
        queue.append((root, 0 ,0))

        while queue:
            length = len(queue)
            for _ in range(length):
                value,row, column = queue.popleft()

                if value.left:
                    queue.append((value.left,row+1, column - 1))
                if value.right:
                    queue.append((value.right,row+1, column+1))

                values_col[column].append((row,value.val))

        vertical_items = sorted(values_col.items())

        for i in range(len(vertical_items)):
            vertical_items[i] = vertical_items[i][1]
        

        for i in range(len(vertical_items)):
            vertical_items[i].sort()
            for j in range(len(vertical_items[i])):
                vertical_items[i][j] = vertical_items[i][j][1]

        return vertical_items
