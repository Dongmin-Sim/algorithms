from tkinter.messagebox import NO
from turtle import st


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next

        return item


# create stack
stack = Stack()


# push
stack.push(1)
stack.push(2)
stack.push(3)

# pop
for _ in range(3):
    print(stack.pop())