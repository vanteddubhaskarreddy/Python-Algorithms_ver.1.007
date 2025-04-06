class StockSpanner:

    def __init__(self):
        self.stack = []
        self.array = []

    def next(self, price: int) -> int:
        self.array.append(price)
        while self.stack and self.array[self.stack[-1]] <= price:
            self.stack.pop()
        self.stack.append(len(self.array) - 1)
        return self.stack[-1]-self.stack[-2] if len(self.stack) > 1 else self.stack[0] + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)