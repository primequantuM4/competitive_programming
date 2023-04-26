class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent

        self.adj_list = defaultdict(list)
        for i in range(len(parent)):
            self.adj_list[parent[i]].append(i)

        self.locked = defaultdict(int)        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False

        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False

        self.locked.pop(num)
        return True

    def upgrade(self, num: int, user: int) -> bool:
        #first check if node is locked
        nodeIsLocked = num in self.locked
        if nodeIsLocked or self.isAncestorLocked(num):
            return False

        stack = [num]
        hasLockedDescendant = False
        while stack:
            cur_node = stack.pop()
            
            for next_node in self.adj_list[cur_node]:
                if next_node in self.locked:
                    hasLockedDescendant = True
                    self.locked.pop(next_node)
                stack.append(next_node)

        if hasLockedDescendant:
            self.locked[num] = user
        print(self.locked)
        return hasLockedDescendant
    
    def isAncestorLocked(self, num):
        value = self.parent[num]
        while value != -1:
            if value in self.locked:
                return True

            value = self.parent[value]

        return False  


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
