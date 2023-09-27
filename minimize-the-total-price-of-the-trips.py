class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        count = defaultdict(int)
        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def calculate(visited, start, end):
            visited.add(start)
            if start == end:
                count[end] += 1
                return True
            for next_node in adj_list[start]:
                if next_node in visited:
                    continue
                if calculate(visited, next_node, end):
                    count[start] += 1
                    return True
            return False
            
        for node_a, node_b in trips:
            calculate(set(),node_a, node_b)
        
        @cache
        def dp(node, parent, used):
            half_cost = count[node] * price[node] // 2
            cur_cost = count[node] * price[node]

            for next_node in adj_list[node]:
                if next_node == parent:
                    continue
                if not used:
                    half_cost += dp(next_node, node, True)
                cur_cost += dp(next_node, node, False)

            if not used:
                return min(half_cost, cur_cost)
            return cur_cost
        
        min_cost = inf
        for i in range(n):
            min_cost = min(min_cost, dp(i, -1, False))
        
        return min_cost

        
        
