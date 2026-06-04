# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        listLen = 0
        node = head
        while node:
            listLen += 1
            node = node.next
        # if listLen == 1:
        #     return None
        index = listLen - n
        start = head
        prev = None
        for i in range(listLen):
            if i == index:
                if prev is None:
                    return start.next
                else:
                    if start.next:
                        prev.next = start.next
                    else:
                        prev.next = None
            prev = start
            start = start.next

        return None if not head else head
                


