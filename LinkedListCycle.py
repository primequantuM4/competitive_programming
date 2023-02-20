# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head

        if(not head):
            return False
        #use two pointers to (floyds detection cycle) to determine if it exists
        slow = head
        fast = head.next
        while(slow != fast):
            if not fast or not fast.next:
                #this means we have finished the list so no cycle
                return False
            slow = slow.next
            fast = fast.next.next
        
        #if by any chance they are equal that means fast caught up with slow I guess?
        return True


        return False
