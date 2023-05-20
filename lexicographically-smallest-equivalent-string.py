class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #make the connected parent the minimum
        words = {}
        answer = ""
        def union(x, y):
            x_rep, y_rep = find(x), find(y)

            if x_rep < y_rep:
                words[y_rep] = words[x_rep] 
            else:
                words[x_rep] = words[y_rep]

        def find(node):
            words.setdefault(node, node)
            if words[node] != node:
                words[node] = find(words[node])
            
            return words[node]
            
        for letter1, letter2 in zip(s1, s2):
            union(letter1, letter2)

        for c in baseStr:
            answer += find(c)
        
        return answer