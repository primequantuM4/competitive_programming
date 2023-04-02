class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast= head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        slow.next = None
        
        operated = self.reverse(second_half)
        maxTwinSum = self.calculateMaxSum(operated, head)

        return maxTwinSum


    def reverse(self, head):
        prev = None
        
        while head:
            head.next,prev,head = prev, head, head.next
        
        return prev
    def calculateMaxSum(self, operated, head):
        value = 0

        while operated:
            value = max(value, operated.val + head.val)
            operated = operated.next
            head = head.next
        
        return value
