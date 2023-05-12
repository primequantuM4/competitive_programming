class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque([])
        visited = set()
        depth_level = defaultdict(int)
        answer = []
        
        for node, another_node in edges:
            graph[node].append(another_node)
            graph[another_node].append(node)
            indegree[node] += 1
            indegree[another_node] += 1

        for node in range(n):
            if indegree[node] == 1:
                queue.append((node, 0))
                visited.add(node)
                depth_level[node] = 0

        while queue:            
            cur_node, depth = queue.popleft()
            depth_level[cur_node] = depth

            for next_node in graph[cur_node]:
                if next_node not in visited:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 1:
                        queue.append((next_node, depth + 1))
                        visited.add(next_node)

        max_score_node = max(depth_level, key=lambda x: depth_level[x])
        answer.append(max_score_node)

        for node in range(n):
            if depth_level[node] == depth_level[max_score_node] and node != max_score_node:
                answer.append(node)

        return answer
