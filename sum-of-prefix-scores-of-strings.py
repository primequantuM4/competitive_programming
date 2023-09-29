class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.prefix_count = 0
        self.end_count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.prefix_count += 1