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
    public ListNode partition(ListNode head, int x) {

        if (head == null) return null;
        if(head.next == null) return head;

        ListNode greaterList = new ListNode();
        ListNode lessList = new ListNode();
        ListNode current = head;
        ListNode lessPtr = lessList;
        ListNode greaterPtr = greaterList;

        while (current != null){
            if (current.val < x){
                lessPtr.next = current;
                lessPtr = lessPtr.next;
            }else{
                greaterPtr.next = current;
                greaterPtr = greaterPtr.next;
            }
            current = current.next;
        }
        greaterPtr.next = null;
        lessPtr.next = greaterList.next;

        return lessList.next;
    }
}
