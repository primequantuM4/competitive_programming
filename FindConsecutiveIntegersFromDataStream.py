class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.q = deque()
        self.size = k
        self.similar = 0

    def consec(self, num: int) -> bool:
        val = -1
        if num == self.value:
            self.similar += 1
        self.q.append(num)
        
        if len(self.q) > self.size:
            val = self.q.popleft()
    
        if val == self.value:
            self.similar -= 1
        
        return self.similar ==self.size

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
