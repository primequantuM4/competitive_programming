# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, largerNodes = [], []
        node, idx = head, 0

        while node:
            largerNodes.append(0)
            
            while stack and node.val > stack[-1][0]:
                value, index = stack.pop()
                largerNodes[index] = node.val
            
            stack.append((node.val, idx))
            idx += 1
            node = node.next

        return largerNodes
