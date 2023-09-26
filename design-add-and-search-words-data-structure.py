class TrieNode:

    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur_index = ord(char) - 97
            if not cur.children[cur_index]:
                cur.children[cur_index] = TrieNode()
            cur = cur.children[cur_index]

        cur.is_end = True 

    def search(self, word: str) -> bool:
        cur = self.root
        stack = [(cur, 0)]
        valid = False
        
        while stack:
            trie, index = stack.pop()

            if len(word) == index:
                valid = valid or trie.is_end
                continue
            char_index = ord(word[index]) - 97

            if word[index] == ".":
                for i in range(len(trie.children)):
                    if trie.children[i]:
                        stack.append((trie.children[i], index + 1))
                        
            elif trie.children[char_index]:
                stack.append((trie.children[char_index], index + 1))
            
        return valid
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
