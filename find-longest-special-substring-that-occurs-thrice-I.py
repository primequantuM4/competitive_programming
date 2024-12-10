class Solution:
    def maximumLength(self, s: str) -> int:
        val = Counter(s)
        if len(val) == len(s):
            return -1
        
        l_ptr = 0
        tracker = defaultdict(int)
        tracker[s[0]] += 1

        for r_ptr in range(1, len(s)):
            if s[l_ptr] != s[r_ptr]:
                tracker[s[r_ptr]] += 1
                l_ptr = r_ptr
                continue
            
            num_length = r_ptr - l_ptr + 1
            for i in range(1, num_length + 1):
                char = s[l_ptr] * i
                tracker[char] += 1



        max_key = (lambda d: max(
            (k for k, v in d.items() if v >= 3),
         key=len, default=''))(tracker)
        if not max_key:
            return -1
        return len(max_key)
