class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        #since we need to get all the apples I think the path should be the same
        #we start at 0
        self.path = defaultdict(list)
        for parent, child in edges:
            self.path[parent].append(child)
            self.path[child].append(parent)

        def dfs(node, parent):
            cur_path = 0
            total_path = 0
            if not self.path[node]:
                return 0

            for next_path in self.path[node]:
                if parent == next_path:
                    continue

                cur_path = dfs(next_path, node)
            
                if cur_path > 0 or hasApple[next_path]:
                    total_path += cur_path + 2
            
            return total_path

        return dfs(0, -1)

            
