class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incomingEdges = set()
        outgoingEdges = []
        for outgoing, incoming in edges:
            incomingEdges.add(incoming)

        for node in range(n):
            if node not in incomingEdges:
                outgoingEdges.append(node)

        return outgoingEdges
