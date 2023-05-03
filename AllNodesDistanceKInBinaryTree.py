# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #first build an adj_list for easier traversal
        #use pure bfs to build the adj_list
        def bfs(start_node):
            queue = deque([(start_node, 0)])
            visited = {start_node}

            while queue:
                cur_node, dist = queue.popleft()
                if cur_node == target.val and dist == k:
                    return start_node
                
                for next_node in adj_list_representation[cur_node]:
                    if next_node not in visited and dist < k:
                        queue.append((next_node, dist + 1))
                        visited.add(next_node)

        adj_list_representation = defaultdict(list)
        queue = deque([root])
        res, visited = [], set()

        while queue:
            cur_node = queue.popleft()
            if cur_node.left:
                adj_list_representation[cur_node.val].append(cur_node.left.val)
                adj_list_representation[cur_node.left.val].append(cur_node.val)
                queue.append(cur_node.left)

            if cur_node.right:
                adj_list_representation[cur_node.val].append(cur_node.right.val)
                adj_list_representation[cur_node.right.val].append(cur_node.val)
                queue.append(cur_node.right)

        for key in adj_list_representation.keys():
            x = bfs(key)
            if x is not None:
                res.append(x)
        



        return res




