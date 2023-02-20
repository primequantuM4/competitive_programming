# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #.next.next -> odd from head
        #.next -> even
        #both go .next.next though
        if not head:
            return
        if not head.next:
            return head
        current = head
        odd = ListNode()
        even = ListNode()
        count = 1

        odd_ptr = odd
        even_ptr = even
        while current:
            if count % 2 == 1:
                odd_ptr.next = current
                odd_ptr = odd_ptr.next
            else:
                even_ptr.next = current
                even_ptr = even_ptr.next

            count += 1
            current = current.next

        even_ptr.next = None
        odd_ptr.next = even.next

        return odd.next
