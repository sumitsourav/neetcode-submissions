# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        pq = []
        i = 0
        for arrnode in lists:
            while arrnode:
                heapq.heappush(pq, (arrnode.val, i, arrnode))
                arrnode = arrnode.next
                i = i + 1
        while pq:
            val, i, node = heapq.heappop(pq)
            current.next = node
            current = current.next
        return dummy.next
