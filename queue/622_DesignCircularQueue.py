class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.head, self.tail = 0, 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.tail] is None:
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % self.maxlen
            return True
        
        return False
        

    def deQueue(self) -> bool:
        if self.q[self.head] is None:
            return False
        
        self.q[self.head] = None
        self.head = (self.head + 1) % self.maxlen
        
        return True
        

    def Front(self) -> int:
        return self.q[self.head] if self.q[self.head] is not None else -1
        

    def Rear(self) -> int:
        return self.q[self.tail - 1] if self.q[self.tail - 1] is not None else -1
        

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.q[self.head] is None
        

    def isFull(self) -> bool:
        return self.head == self.tail and self.q[self.head] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()