class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #return when you can find a path between them
        arr = [i for i in range(1, len(edges)+ 1)]
        def find(x, y):
            while x != arr[x - 1]:
                x = arr[x - 1]
            
            while y != arr[y - 1]:
                y = arr[y - 1]

            return x, y
        ans = []
        for node_a, node_b in edges:
            rep_a, rep_b = find(node_a, node_b)
            if rep_a == rep_b:
                ans = [node_a, node_b]
            else:
                orignal_rep = arr[node_b - 1]
                arr[node_b - 1] = arr[node_a - 1]
                for i in range(len(arr)):
                    if arr[i] == orignal_rep:
                        arr[i] = arr[node_a - 1]
        return ans
        