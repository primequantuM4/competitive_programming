class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u,v,w in times:
            adj_list[u].append((v, w))
        visited = set()
        shortest = [inf for _ in range(n)]
        heap = [(0, k)]

        while heap:
            t, node = heappop(heap)
            if node in visited:
                continue
            
            shortest[node - 1] = t
            visited.add(node)

            for next_node, weight in adj_list[node]:
                heappush(heap, (weight + t, next_node))
        
        return -1 if max(shortest) == inf else max(shortest)

        
