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
        for i in range(n - 1, -1, -1):
            start_again.val = stack[i]
            start_again = start_again.next
        return head

