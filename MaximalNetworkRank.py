class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        maximum_network = 0

        for city_a, city_b in roads:
            adj_list[city_a].append(city_b)
            adj_list[city_b].append(city_a)

        for node in range(n):
            node_set = set(adj_list[node])
            for another_node in range(n):
                if node == another_node:
                    continue

                currentLength = len(adj_list[node]) + len(adj_list[another_node])
                if another_node in node_set:
                    currentLength -= 1

                maximum_network = max(maximum_network, currentLength)

        return maximum_network

