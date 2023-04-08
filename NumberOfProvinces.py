class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        number_of_provinces = 0
        visited = set()

        for row in range(len(isConnected)):
            if row not in visited:
                visited.union(self.dfs(row, isConnected, visited))

                number_of_provinces += 1

        return number_of_provinces
    
    def dfs(self,start, graph, visited):
        stack = []
        stack.append(start)

        while stack:
            cur_row = stack.pop()

            for col in range(len(graph)):
                if graph[cur_row][col] and col not in visited:
                    stack.append(col)
            
            visited.add(cur_row)
        
        return visited

