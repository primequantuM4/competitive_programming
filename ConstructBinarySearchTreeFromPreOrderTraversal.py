# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder_arr = sorted(preorder.copy())
        num_indexes = {}
        for i in range(len(inorder_arr)):
            num_indexes[inorder_arr[i]] = i
        self.root_index = 0
        def constructBst(left, right):
            if left == right:
                return None
            root_node = TreeNode(preorder[self.root_index])
            self.root_index += 1
            parent_index = num_indexes[root_node.val]

            root_node.left = constructBst(left, parent_index)
            root_node.right = constructBst(parent_index + 1, right)
            return root_node

        return constructBst(0, len(preorder))
