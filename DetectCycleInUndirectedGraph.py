from typing import List
from collections import defaultdict, deque
class Solution:
#Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        indegree = defaultdict(int)
        queue = deque([])
        visited = set()
        for node in range(len(adj)):
            indegree[node] += len(adj[node])
    
        for nodes in range(V):
            if indegree[nodes] == 1:
                queue.append(nodes)
                visited.add(nodes)
    
        while queue:
            node = queue.popleft()
            for next_node in adj[node]:
                if next_node not in visited:
                    indegree[next_node] -= 1
                    if indegree[next_node] <= 1:
                        queue.append(next_node)
                        visited.add(next_node)
                
        for n in range(V):
            if indegree[n] > 1:
                return 1

        return 0
