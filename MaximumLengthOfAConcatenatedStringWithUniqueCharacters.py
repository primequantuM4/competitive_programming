class Solution:
    def maxLength(self, arr: List[str]) -> int:
        #use sets I guess
        max_unique = set()
        self.max_number = 0
        def backtrack(level):
            if max_unique:
                self.max_number = max(self.max_number, len(max_unique))

            for i in range(level, len(arr)):
                new_set = set(map(str, arr[i]))
                intersection = max_unique.intersection(new_set)
                maximum = Counter(arr[i])
                if not intersection and len(maximum) == len(arr[i]):
                    for j in arr[i]:
                        max_unique.add(j)
                    backtrack(i+1)
                    for j in arr[i]:
                        max_unique.remove(j)
        backtrack(0)
        return self.max_number
        
