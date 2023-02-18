# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #first know the linked list length I guess?
        linked_list_length = 0
        current = head

        while current:
            linked_list_length += 1
            current = current.next

        removed_node_index = linked_list_length - n - 1
        removed = head

        if n == linked_list_length:
            return head.next

        if linked_list_length == 1:
            return None
            
        for i in range(removed_node_index):
            removed = removed.next
           

        removed.next = removed.next.next

        return head
