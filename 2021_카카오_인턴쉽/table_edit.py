class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Linkedlist:
    def __init__(self):
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.tail.prev = 

        self.num_of_data += 1

    def first(self):
        if self.num_of_data == 0:
            return None
        
        self.before = self.head
        self.current = self.head.next

    def next(self):
        if self.current.next == None:
            return None
        
        self.before = self.current
        self.current = self.current.next

    def before(self):
        if self.before == self.head:
            return None
        
        self.current = self.before
        self.before = 

    def select(self, dir, num):
        if dir == 'U':
            pass

        if dir == 'D':
            pass

        pass

    def delete(self):
        pass


link_list = Linkedlist()
link_list.append(1)
link_list.append(2)
link_list.append(3)
link_list.append(4)
link_list.append(5)
link_list.append(6)

link_list.first()
for _ in range(2):
    link_list.next()

print(link_list.current.data)

