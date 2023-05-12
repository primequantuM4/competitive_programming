class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        numbers = set()
        visited = set()
        ordered_num = []
        stack = []

        for num1, num2 in adjacentPairs:
            graph[num1].append(num2)
            graph[num2].append(num1)
            numbers.add(num1)
            numbers.add(num2)

            indegree[num1] += 1
            indegree[num2] += 1
        
        for num in numbers:
            if indegree[num] == 1:
                queue.append(num)
                visited.add(num)

        while stack:
            cur_num = queue.pop()
            ordered_num.append(cur_num)

            for next_num in graph[cur_num]:
                if next_num not in visited:
                    indegree[next_num] -= 1
                    if indegree[next_num] == 1:
                        queue.append(next_num)

        return ordered_num
