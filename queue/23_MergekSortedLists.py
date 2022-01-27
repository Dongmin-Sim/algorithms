# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        
        heap = []
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
            
        while heap:
            node = heapq.heappop(heap)
            result.next = node[2]
            
            result = result.next
            
            if result.next:
                heapq.heappush(heap, (result.next.val, node[1], result.next))
            
        
        return root.next