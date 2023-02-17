# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        current = head

        while current is not None:
            values.append(current.val)
            current = current.next

        if not values:
            return
        reversedHead = ListNode(values[-1])
        current = reversedHead
        for i in range(len(values)-2, -1, -1):
            current.next = ListNode(values[i])
            current = current.next


        return reversedHead
