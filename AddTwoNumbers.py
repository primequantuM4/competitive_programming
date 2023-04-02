# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy

        running_sum = 0

        while l1 or l2:
            if l1:
                running_sum += l1.val
                l1 = l1.next

            if l2:
                running_sum += l2.val
                l2 = l2.next
            
            ptr.next = ListNode(running_sum % 10)
            ptr = ptr.next

            running_sum = 0 if running_sum <= 9 else 1
        
        if running_sum: #we have a carry
            ptr.next = ListNode(running_sum)
        
        return dummy.next
