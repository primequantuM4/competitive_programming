class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        similar_node_count = [1] * n
        #process the input
        adj_list = defaultdict(list)
        for node, another_node in edges:
            adj_list[node].append(another_node)
            adj_list[another_node].append(node)

        def dfs(node, parent):
            is_leaf_node = len(adj_list[node]) == 1 and parent == adj_list[node][0]
            if is_leaf_node:
                return Counter(labels[node])

            cur_dict = Counter()
            for next_node in adj_list[node]:
                if next_node != parent:
                    cur_dict += dfs(next_node, node)
            occurences = cur_dict[labels[node]]
            similar_node_count[node] += occurences

            cur_dict[labels[node]] += 1
            return cur_dict

        dfs(0, -1)
        return similar_node_count
