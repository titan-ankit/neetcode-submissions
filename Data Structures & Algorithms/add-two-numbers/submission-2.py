# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        prev1 = None
        while current1:
            nxt = current1.next
            current1.next = prev1
            prev1 = current1
            current1 = nxt
        current1 = prev1
        # now current1 is at the tail , last valid digit
        s1 = ""
        while current1:
            s1 += str(current1.val)
            current1 = current1.next
    
        current2 = l2
        prev2 = None
        while current2:
            nxt = current2.next
            current2.next = prev2
            prev2 = current2
            current2 = nxt
        current2 = prev2
        s2 = ""
        while current2:
            s2 += str(current2.val)
            current2 = current2.next

        sum = int(s1) + int(s2)

        if sum == 0:
            return ListNode(0)

        start = ListNode()
        current = start
        while sum>0:
            digit = sum % 10        
            current.next = ListNode(digit)   
            current = current.next                
            sum = sum // 10

        return start.next
