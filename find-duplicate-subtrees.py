# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        duplicate_sub_tree = defaultdict(int) 
        trees = []

        def traverse(node):
            if not node:
                return 
            
            cur_tree = self.change_to_tuple(node)
            traverse(node.left)
            traverse(node.right)

            duplicate_sub_tree[cur_tree] += 1
            if duplicate_sub_tree[cur_tree] == 2:
                trees.append(node)
        
        traverse(root)
        return trees
    def change_to_tuple(self, node):
        tree = []
        queue = deque([node])

        while queue:
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if not cur_node:
                    tree.append(-201)
                    continue

                tree.append(cur_node.val)
                queue.append(cur_node.left)
                queue.append(cur_node.right)
        
        return tuple(tree)