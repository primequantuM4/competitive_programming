class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestor = defaultdict(set)
        indegree = defaultdict(int)

        queue = deque([])
        ancestorList = []
        for outgoing, incoming in edges:
            graph[outgoing].append(incoming)
            indegree[incoming] += 1
            ancestor[incoming].add(outgoing)

        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            cur_node = queue.popleft()

            for next_node in graph[cur_node]:
                indegree[next_node] -= 1
                ancestor[next_node].update(ancestor[cur_node])
                if indegree[next_node] == 0:
                    queue.append(next_node)

            
        for node in range(n):
            ancestorList.append(sorted(list(ancestor[node])))

        return ancestorList
