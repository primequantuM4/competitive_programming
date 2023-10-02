class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj_list = defaultdict(list)
        for sink, source in enumerate(parent):
            adj_list[source].append(sink)

        self.max_dist = 1

        def dfs(cur_node):
            high_score = [0, 0] 
            for next_node in adj_list[cur_node]:
                if s[next_node] == s[cur_node]:
                    high_score.append(0)
                    dfs(next_node)
                    continue

                value = dfs(next_node)
                high_score.append(value)
            
            high_score.sort()
            cur_max = 1 + high_score[-1] + high_score[-2]
            self.max_dist = max(cur_max, self.max_dist)
            return 1 + high_score[-1]
        
        dfs(0)
        return self.max_dist


        