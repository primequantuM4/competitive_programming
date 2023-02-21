/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode dummyPtr = dummy;

        while(head != null){
            if(head.next != null && head.val == head.next.val){
                int value = head.val;
                while(head.next != null && head.next.val == value){
                    head = head.next;
                }
                dummyPtr.next = head.next;
            }else{
                dummyPtr = dummyPtr.next;
            }
            head = head.next;
        }
        return dummy.next;
    }
}
