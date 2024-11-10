class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.current_sum = 0
        

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            oldest = self.queue.popleft()
            self.current_sum -= oldest
        self.queue.append(val)
        self.current_sum += val

        return self.current_sum / len(self.queue)

"""
TIME COMPLEXITY: O(1)
1. For each next call because adding and removing elements from a deque,
as well as updating the sum, takes constant time

SPACE COMPLEXITY: O(N)
1. Where n is the size of the current sliding window, as we store atmost n elements in the queue

"""
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)