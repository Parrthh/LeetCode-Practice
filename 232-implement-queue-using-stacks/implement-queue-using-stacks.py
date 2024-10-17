class MyQueue:

    def __init__(self):
        # Initializing two stacks
        self.stack1 = []            # Stack1 is used for enqueueing operation
        self.stack2 = []            # Stack2 is used for dequeueing operation
        
    def push(self, x: int) -> None:
        self.stack1.append(x)       # We push elements into Stack1
    
    def pop(self) -> int:
        if not self.stack2:         # If Stack2 is empty, we pop elements from stack1
            while self.stack1:      # When Stack1 is not empty
                self.stack2.append(self.stack1.pop())       # We pop elements from stack1 and append it to Stack2
        return self.stack2.pop()    # Returning the popped elements the way they are handled in queue based implementation
        
    def peek(self) -> int:
        if not self.stack2:         # If Stack2 is empty, we pop elements from stack1
            while self.stack1:      # When Stack1 is not empty
                self.stack2.append(self.stack1.pop())       # We pop elements from stack1 and append it to Stack2
        return self.stack2[-1]     # As here we just need the first element
        
    def empty(self) -> bool:        # Checking if both the queues are empty
        return not self.stack1 and not self.stack2
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()