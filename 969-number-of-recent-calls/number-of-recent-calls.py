class RecentCounter:

    def __init__(self):
        self.queue = collections.deque()
        # self.counter = [null]

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[-1] - self.queue[0] > 3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)