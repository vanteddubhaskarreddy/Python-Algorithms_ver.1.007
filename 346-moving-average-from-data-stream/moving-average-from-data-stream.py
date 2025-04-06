class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.queue.popleft()
        return sum(self.queue)/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)