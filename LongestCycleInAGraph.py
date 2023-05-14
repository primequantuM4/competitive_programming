class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False]* n
        indegree = [0] * n

        for edge in edges:
            if edge != -1:
                indegree[edge] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            visited[node] = True

            next_node = edges[node]
            if next_node != -1:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)

        answer = -1
        for i in range(n):
            if not visited[i]:
                neighbor = edges[i]
                count = 1
                visited[i] = True
                while neighbor != i:
                    visited[neighbor] = True
                    count += 1
                    neighbor = edges[neighbor]
                answer = max(answer, count)

        return answer


