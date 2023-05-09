class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create dependency graph
        if not prerequisites:
            return True

        requisitesDependencies = defaultdict(list)
        inDegree = defaultdict(int)
        courses = 0
        courses_to_learn = 0

        queue = deque([])

        for cur_course, pre_course in prerequisites:
            inDegree[cur_course] += 1
            courses_to_learn += 1
            requisitesDependencies[pre_course].append(cur_course)

        for course in requisitesDependencies.keys():
            if inDegree[course] == 0: #means that we have a starting node for multisource bfs
                queue.append(course)

        while queue:
            cur_class = queue.popleft()

            for next_course in requisitesDependencies[cur_class]:
                courses += 1
                inDegree[next_course] -= 1
                if inDegree[next_course] == 0:
                    queue.append(next_course)

        if courses == courses_to_learn:
            return True

        return False
