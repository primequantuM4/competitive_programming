class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        visited = set()
        adj_list = defaultdict(list)
        self.ans = 0

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node):
            visited.add(node)
            cur_sum = values[node]

            for next_node in adj_list[node]:
                if next_node in visited:
                    continue
                
                remaining = dfs(next_node)
                if remaining % k == 0:
                    self.ans += 1
                else:
                    cur_sum += remaining
                
            return cur_sum
        
        dfs(0)
    
        return self.ans + 1
        