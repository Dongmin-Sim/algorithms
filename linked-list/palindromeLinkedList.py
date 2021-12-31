# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        p_list = []
        
        if not head:
            return True
        
        node = head
        while node is not None:
            p_list.append(node.val)
            node = node.next
            
        while (len(p_list)) > 1:
            if p_list.pop() != p_list.pop(0):
                return False
            
        return True