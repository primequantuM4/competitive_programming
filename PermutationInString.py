class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        checked = Counter(s1)
        compared = defaultdict(int)
        dummy = []
        left = 0

        for right in range(len(s2)):
            compared[s2[right]] += 1
            dummy.append(0)
            while len(dummy) > len(s1):
                compared[s2[left]] -= 1
                if not compared[s2[left]]: 
                    del(compared[s2[left]])
                left += 1
                dummy.pop()
            
            if compared == checked:
                return True
        
        return False
