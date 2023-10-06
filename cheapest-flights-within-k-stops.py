class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        shortest = defaultdict(lambda:inf)
        for cur, to, price in flights:
            adj_list[cur].append((to, price))
        
        heap = [(0,0, src)]
        visited = defaultdict(int)
        visited[src] = 0


        while heap:
            k_stop,price,node = heappop(heap)
            if k_stop > k:
                break
            for next_node, next_price in adj_list[node]:
                if next_node not in visited or visited[next_node] > price + next_price:
                    visited[next_node] = price + next_price
                    heappush(heap, ( k_stop + 1, price + next_price, next_node))

        return visited[dst] if dst in visited else -1
        
