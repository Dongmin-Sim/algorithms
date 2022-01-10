# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
            
        return head
    
    
    
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        
        prev.next = head
        
        while head and head.next:
            # a(head)가 b의 다음 노드를 가리키도록 pointer 변경
            # b가 a(head)를 가리키도록 pointer 변경
            b = head.next
            head.next = b.next
            b.next = head
            
            # a(head)이전의 prev가 바뀐 b를 가리키도록 변경
            prev.next = b
            
            # head, prev 재설정
            head = head.next
            prev = prev.next.next
        
        return root.next


class Solution3:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            
            p.next = head
            return p

        return head