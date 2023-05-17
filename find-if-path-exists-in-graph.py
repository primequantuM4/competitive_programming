class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        arr = [i for i in range(n)]

        def union(x, y):
            while arr[x] != x:
                x = arr[x]
            while arr[y] != y:
                y = arr[y]
                
            arr[y] = arr[x]

        def find(x, y):
            while arr[x] != x:
                x = arr[x]

            while arr[y] != y:
                y = arr[y]

                
            
            return arr[x] == arr[y]

        for node_a, node_b in edges:
            union(node_a, node_b)

        return find(source, destination)