class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #create an adj list
        adj_list = {}
        for i in range(len(bombs)):
            x1, y1, radius1 = bombs[i]
            adj_list[i] = []
            for j in range(len(bombs)):
                x2, y2, radius2 = bombs[j]
                lineLength = math.sqrt(((x2-x1) ** 2) + ((y2-y1) **2)) 
                if lineLength <= radius1:
                    adj_list[i].append(j)

        def dfs(node):
            max_detonator = 1
            stack = [node]
            bombs_detonated = 0
            visited = set()
            visited.add(node)

            while stack:
                cur_node = stack.pop()
                bombs_detonated += 1
                max_detonator = max(max_detonator, bombs_detonated)

                for next_node in adj_list[cur_node]:
                    if next_node not in visited:
                        stack.append(next_node)
                        visited.add(next_node)

            return max_detonator

        max_reaching_dist = 1
        for bomb in range(len(bombs)):
            max_reaching_dist = max(max_reaching_dist, dfs(bomb))

            
        return max_reaching_dist
