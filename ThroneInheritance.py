class ThroneInheritance:

    def __init__(self, kingName: str):
        self.starter = kingName
        self.relationship = {}
        self.alive = {}       

        self.relationship[kingName] = []
        self.alive[kingName] = True

    def birth(self, parentName: str, childName: str) -> None:
        self.relationship[parentName].append(childName)
        self.relationship[childName] = []

        self.alive[childName] = True

    def death(self, name: str) -> None:
        self.alive[name] = False

    def getInheritanceOrder(self) -> List[str]:
        stack = [self.starter]
        successors = []

        while stack:
            cur_person = stack.pop()
            children = self.relationship[cur_person]

            if self.alive[cur_person]:
                successors.append(cur_person)
            for child in children[::-1]:
                stack.append(child)

        return successors


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
