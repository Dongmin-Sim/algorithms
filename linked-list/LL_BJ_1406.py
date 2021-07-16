# https://www.acmicpc.net/problem/1406
# 참고 : https://hbj0209.tistory.com/25

class Node:
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data = data
        self.next = next


class DLinked:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(self.head, None, None)

        self.head.next = self.tail

        self.current = self.tail
        self.before = None

    def append(self, data):  # current는 계속 tail
        new_node = Node(None, data, None)

        pre = self.tail.prev

        pre.next = new_node
        self.tail.prev = new_node

    def select(self, dir):
        if dir == 'L':
            self.current = self.current.prev

        if dir == 'D':

            self.current = self.current.next


dlink = DLinked()
dlink.append(3)
dlink.append(5)

print(dlink.current.prev.data)
print(dlink.current.data)
print(dlink.current.next)
