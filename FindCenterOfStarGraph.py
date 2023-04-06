class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        possible_central = set()

        for node_a, node_b in edges:
            if node_a in possible_central:
                return node_a

            elif node_b in possible_central:
                return node_b

            possible_central.add(node_a)
            possible_central.add(node_b)

        return
