class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n
        safeNodes = []

        def addSafeStates(node):
            if color[node] == 1:
                return False

            if color[node] == 2:
                return True
            
            color[node] = 1 # we are processing the node
            for next_node in graph[node]:
                hasCycle = not addSafeStates(next_node)
                if hasCycle:
                    return False
                
                addSafeStates(next_node)
            
            color[node] = 2
            safeNodes.append(node)
            return True

        
        for node in range(n):
            if color[node] != 2:
                addSafeStates(node)

        safeNodes.sort()
        return safeNodes
