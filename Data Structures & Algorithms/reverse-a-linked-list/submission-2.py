# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        stack = []
        while start:
            stack.append(start.val)
            start = start.next
        start_again = head
        n = len(stack)
        while stack:
            start_again.val = stack.pop()
            start_again = start_again.next
        return head

