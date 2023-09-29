class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
        self.is_end = False
    
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.visited = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.root

        if key not in self.visited:
            for char in key:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
                cur.prefix_count += val
            
            cur.is_end = True
            self.visited[key] = val
        else:
            for char in key:
                cur = cur.children[char]
                cur.prefix_count += (val - self.visited[key])
            self.visited[key] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.prefix_count 
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
