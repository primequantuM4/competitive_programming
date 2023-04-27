class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadPaths = set()
        for deadend in deadends:
            deadPaths.add(deadend)

        def nextNodes(node):
            next_nodes = []
            for i in range(4):
                key =  int(node[i])
                for next_key in (-1, 1):
                    comb = (key + next_key) % 10
                    next_nodes.append(node[:i] + str(comb) + node[i+1:])

            return next_nodes

        start = '0000'
        visited = set(['0000'])
        queue = deque([(start, 0)])

        while queue:
            currentKey, level = queue.popleft()

            if currentKey == target:
                return level
            if currentKey in deadPaths:
                continue
            for nextKey in nextNodes(currentKey):
                if nextKey not in visited:
                    visited.add(nextKey)
                    queue.append((nextKey, level + 1))


        return -1
