# Definition for singly-linked list.
from typing import Optional
import functools

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reversedList(l1))
        b = self.toList(self.reversedList(l2))
        
        a = int(''.join(str(i)for i in a))
        b = int(''.join(str(i)for i in b))

        # map + join
        # a = int(''.join(map(str, a)))
        # b = int(''.join(map(str, b)))
        
        # functools
        # a = functools.reduce(lambda x, y: (x * 10) + y, a, 0)
        # b = functools.reduce(lambda x, y: (x * 10) + y, b, 0)

        c = a + b
        
        ans = self.toLinkedList(str(c))
        
        return ans
    
    def reversedList(self, head):
        node, prev = head, None
        
        while node:
            temp, node.next = node.next, prev
            prev, node = node, temp
            
        return prev
    
    def toList(self, node):
        temp = []
        
        while node:
            temp.append(node.val)
            node = node.next
        return temp
    
    def toLinkedList(self, nums):
        temp: ListNode = None
        # temp = ListNode(None)
        
        for num in nums:
            node = ListNode(num)
            node.next = temp 
            temp = node
            
            
        return node
    
            
        
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next