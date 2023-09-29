class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.is_end = True
    def search(self, word) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.is_end            

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))
        if len(words[0]) != 1:
            return ""
        long_word = ""
        trie = Trie()
        for i in words:
            if len(i) == 1:
                trie.insert(i)
                if len(long_word) < len(i):
                    long_word = i
            else:
                is_inserted = trie.search(i[:len(i) - 1])
                if is_inserted:
                    trie.insert(i)
                    long_word = i if len(long_word) < len(i) else long_word
        
        return long_word
          