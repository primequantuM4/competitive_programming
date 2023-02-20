# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        
        if(not head):
            return None
        #use two pointers to (floyds detection cycle) to determine if it exists
        slow = head
        fast = head
        are_different = True
        while(are_different):
            if not fast or not fast.next:
                #this means we have finished the list so no cycle
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                are_different = False

        fast = head
    
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
