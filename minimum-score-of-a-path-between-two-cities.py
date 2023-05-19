class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        path_score = {i:1 for i in range(1, n + 1)}
        tree = {i:i for i in range(1, n + 1)}
        path_costs = []
        # unionize

        def getParent(node):
            path_node = []
            while node != tree[node]:
                path_node.append(node)
                node = tree[node]

            for x in path_node:
                tree[x] = node

            return node
        for node_a, node_b, path_cost in roads:
            node_a = getParent(node_a)
            node_b = getParent(node_b)

            if path_score[node_a] > path_score[node_b]:
                path_score[node_a] += path_score[node_b]
                tree[node_b] = tree[node_a]

            else:
                path_score[node_b] += path_score[node_a]
                tree[node_b] = tree[node_a]

        node_one = getParent(1)

        for node_a, _, path_cost, in roads:
            node_x= getParent(node_a)
            if node_x  == node_one:
                path_costs.append(path_cost)

        return min(path_costs)