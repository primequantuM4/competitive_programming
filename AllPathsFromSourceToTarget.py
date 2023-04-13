class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #adj list maybe but not necessary
        goal_node = len(graph) - 1

        stack = [(0, [0])]
        paths = []

        while stack:
            cur_node, current_path = stack.pop()

            if cur_node == goal_node:
                paths.append(current_path[:])

            for neighbor in graph[cur_node]:
                current_path.append(neighbor)
                stack.append((neighbor, current_path[:]))

                current_path.pop()

        return paths
