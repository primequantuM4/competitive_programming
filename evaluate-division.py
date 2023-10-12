class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)

        for (dividend, divisor), value in zip(equations, values):
            adj_list[dividend].append((divisor, value))
            adj_list[divisor].append((dividend, 1 / value))
        
        def bfs(start, goal):
            visited = {start}
            queue = deque([(start, 1)])

            while queue:
                node, prod = queue.popleft()
                if node == goal:
                    return prod
                
                if node in adj_list:
                    for next_node, wei in adj_list[node]:
                        if next_node not in visited:
                            queue.append((next_node, prod * wei))
                            visited.add(next_node)
            return -1
        
        res = []
        for a, b in queries:
            if a not in adj_list or b not in adj_list:
                res.append(-1)
            elif a == b:
                res.append(1)
            else:
                res.append(bfs(a, b))
        return res
