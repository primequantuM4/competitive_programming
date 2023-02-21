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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return null;
        if(head.next == null) return head;
       
       ListNode old = head;
       int length = 1;
       while (old.next != null){
            old = old.next;
            length++;
       }
       old.next = head;
       ListNode newTail = head;
       for(int i = 0; i < length - k % length - 1; i++){
           newTail = newTail.next;
       }
       ListNode newHead = newTail.next;
       newTail.next = null;

       return newHead;
    }
}
