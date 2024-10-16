class ListNode():
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev  = val, nxt, prev

class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k
        # Initializing a doubly linked list of two dummy nodes
        # Here, the default value is 0, next -> None, prev -> None
        self.left = ListNode(0, None, None)
        # Here, the defaul value is 0, next-> None, prev -> self.left
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space -= 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

        

    def Front(self) -> int:
        # First we have to make sure it is not empty
        if self.isEmpty():
            return -1
        return self.left.next.val
        
    def Rear(self) -> int:
        # First we have to make sure it is not empty
        if self.isEmpty():
            return -1
        return self.right.prev.val
        

    def isEmpty(self) -> bool:
        if self.left.next == self.right: return True
        else: return False
        
    def isFull(self) -> bool:
        return self.space == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()