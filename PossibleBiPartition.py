class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        hatingGraph = defaultdict(list)
        color = {}

        def dfs(personHater):
            stack = [personHater]
            color[person] = 0
            while stack:
                cur_person = stack.pop()

                for hatedPeople in hatingGraph[cur_person]:
                    if hatedPeople not in color:
                        stack.append(hatedPeople)
                        color[hatedPeople] = color[cur_person] ^ 1
                    elif color[hatedPeople] == color[cur_person]:
                        return False
                        

            return True
            
        for person, hated in dislikes:
            hatingGraph[person].append(hated)
            hatingGraph[hated].append(person)
    
        for person in range(1, n + 1):
            if person not in color:
                haveCommonEnemy = not dfs(person)
                if haveCommonEnemy:
                    return False

        return True
