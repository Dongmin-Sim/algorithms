# https://www.acmicpc.net/problem/1158

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node('head')
        self.head.next = self.head
        self.current = self.head
        self.before = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.current.next = new_node
        self.current = new_node

        self.num_of_data += 1

    def select(self, n):
        for _ in range(n):
            if self.current.next.data == 'head':
                self.before = self.current
                self.current = self.current.next
            self.before = self.current
            self.current = self.current.next

    def first(self):
        if self.num_of_data == 0:
            return None

        self.before = self.head
        self.current = self.before.next

    def delete(self):
        pop_data = self.current.data

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_data -= 1

        return pop_data


n, k = map(int, input().split())

link = LinkedList()
result = []

for i in range(1, n + 1):
    link.append(i)

link.first()
link.select(k-1)

while link.num_of_data > 0:
    result.append(str(link.delete()))
    link.select(k)

print('<%s>' % (', '.join(result)))
