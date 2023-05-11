from collections import defaultdict, deque
#User function Template for python3

class Solution:
    def findOrder(self,alien_dict, N, K):
        # code here
        # build the graph
        graph = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque([])
        all_letter = set()
        char_order = []
        for word in range(len(alien_dict) - 1):
            cur_word = alien_dict[word]
            next_word = alien_dict[word + 1]

            min_len = min(len(cur_word), len(next_word))
            for ptr in range(min_len):
                if cur_word[ptr] == next_word[ptr]:
                    continue

                graph[cur_word[ptr]].append(next_word[ptr])
                indegree[next_word[ptr]] += 1
                break

        for word in alien_dict:
            for char in word:
                all_letter.add(char)

        for character in all_letter:
            if indegree[character] == 0:
                queue.append(character)

        while queue:
            cur_char = queue.popleft()
            char_order.append(cur_char)
            for next_char in graph[cur_char]:
                indegree[next_char] -= 1

                if indegree[next_char] == 0:
                    queue.append(next_char)

        
        return "".join(char_order)
     


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
