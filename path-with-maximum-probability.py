class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            w = succProb[i]
            adj_list[u].append((v,w))
            adj_list[v].append((u, w))

        heap = [(-1, start_node)]
        visited = {i:inf for i in range(n)}
        visited[start_node] = 0
        while heap:
            prob, node = heappop(heap)
            
            for next_node, cost in adj_list[node]:
                if next_node not in visited or visited[next_node] > cost * prob:
                    visited[next_node] = cost * prob
                    heappush(heap, (cost * prob, next_node))
        


        return -1 * visited[end_node] if visited[end_node] != inf else 0
        