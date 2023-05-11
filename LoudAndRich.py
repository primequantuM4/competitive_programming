class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        indegree = defaultdict(int)

        queue = deque([])
        answer = [i for i in range(n)]

        for outgoing, incoming in richer:
            graph[outgoing].append(incoming)
            indegree[incoming] += 1

        for node in range(n):
            if indegree[node] == 0:
                queue.append(node)

        while queue:
            cur_node = queue.popleft()

            for next_node in graph[cur_node]:
                indegree[next_node] -= 1
                if quiet[answer[next_node]] > quiet[answer[cur_node]]:
                    answer[next_node] = answer[cur_node]

                if indegree[next_node] == 0:
                    queue.append(next_node)

        return answer




        
