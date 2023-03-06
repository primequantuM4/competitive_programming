class StockSpanner:

    def __init__(self):
        self.stack = []
        self.price_arr = []
        self.index = 0

    def next(self, price: int) -> int:
        while self.stack and self.price_arr[self.stack[-1]] <= price:
            self.stack.pop()

        self.stack.append(self.index)
        self.index += 1
        self.price_arr.append(price)

        if len(self.stack) == 1:
            return self.stack[-1] + 1
        return self.stack[-1] - self.stack[-2]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
