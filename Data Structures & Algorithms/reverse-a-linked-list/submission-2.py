# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # tail points to null
        current = head
        while (current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        #current is null now, prev is at last item in list (need to make this the head)
        head = prev
        return head


